"""
NP2.0 in SpikeInterface
=======================

Sara Mederos
`(Hofer Lab) <https://www.sainsburywellcome.org/web/groups/hofer-lab>`__
performs chronic electrophysiological
recordings from subcortical and cortical areas using 4-shank
Neuropixels 2.0 probes (acquired using
`Open Ephys <https://open-ephys.org/>`__).
Recordings are conducted in freely moving mice during behavioral
paradigms that assess the cognitive control of innate behaviors.
A pipeline used for pre-processing, sorting, and quality metrics
can be found below.
"""

from spikeinterface import extract_waveforms
from spikeinterface.extractors import read_openephys
from spikeinterface.preprocessing import phase_shift, bandpass_filter, common_reference
from spikeinterface.sorters import run_sorter
from spikeinterface.qualitymetrics import compute_quality_metrics
from pathlib import Path
from probeinterface.plotting import plot_probe
import matplotlib.pyplot as plt
from spikeinterface import curation
from spikeinterface.widgets import plot_timeseries
import numpy as np


data_path = Path(
    r"/ceph/.../100323/2023-10-03_18-57-09/Record Node 101/experiment1"
)
output_path = Path(
    r"/ceph/.../derivatives/100323/"
)

show_probe = False
show_preprocessing = True

# This reads OpenEphys 'Binary' format. It determines the
# probe using probeinterface.read_openephys, which reads `settings.xml`
# and requires the NP_PROBE field is filled.
raw_recording = read_openephys(data_path)

if show_probe:
    probe = raw_recording.get_probe()
    plot_probe(probe)
    plt.show()

# Run time shift (multiplex correction) and filter
shifted_recording = phase_shift(raw_recording)
filtered_recording = bandpass_filter(shifted_recording, freq_min=300, freq_max=6000)

# Perform median average filter by shank
channel_group = filtered_recording.get_property("group")
split_channel_ids = [
    filtered_recording.get_channel_ids()[channel_group == idx]
    for idx in np.unique(channel_group)
]
preprocessed_recording = common_reference(
    filtered_recording, reference="global", operator="median", groups=split_channel_ids
)

if show_preprocessing:
    recs_grouped_by_shank = preprocessed_recording.split_by("group")
    for rec in recs_grouped_by_shank:
        plot_timeseries(
            preprocessed_recording,
            order_channel_by_depth=True,
            time_range=(3499, 3500),
            return_scaled=True,
            show_channel_ids=True,
            mode="map",
        )
        plt.show()

# Run the sorting
sorting = run_sorter(
    "kilosort3",
    preprocessed_recording,
    singularity_image=True,
    output_folder=(output_path / "sorting").as_posix(),
    car=False,
    freq_min=150,
)

# Curate the sorting output and extract waveforms. Calculate
# quality metrics from the waveforms.
sorting = sorting.remove_empty_units()

sorting = curation.remove_excess_spikes(sorting, preprocessed_recording)

# The way spikeinterface is set up means that quality metrics are
# calculated on the spikeinterface-preprocessed, NOT the kilosort
# preprocessed (i.e. drift-correct data).
# see https://github.com/SpikeInterface/spikeinterface/pull/1954 for details.
waveforms = extract_waveforms(
    preprocessed_recording,
    sorting,
    folder=(output_path / "postprocessing").as_posix(),
    ms_before=2,
    ms_after=2,
    max_spikes_per_unit=500,
    return_scaled=True,
    sparse=True,
    peak_sign="neg",
    method="radius",
    radius_um=75,
)

quality_metrics = compute_quality_metrics(waveforms)
quality_metrics.to_csv(output_path / "postprocessing")
