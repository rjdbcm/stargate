"""
This file is part of the Stargate project, Copyright Stargate Team

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

"""

from sglib.lib.translate import _


audio_viewer_widget_folders = _(
"""\
Use this tab to browse your folders and files.  Drag and drop one file at a
time onto the sequencer.  .wav and .aiff files are the only supported audio
file format.""")


audio_viewer_widget_papifx = _("""\
This tab allows you to set effects per-audio file.  There will be exactly one
instance of these effects per audio file.  Use this as a mixing aid for EQ,
filter, etc... on a file.""")

audio_viewer_widget_paifx = _("""\
This tab allows you to set effects per-audio-item.  The effects will be unique
per instance of an audio file, and not share between instances.""")

timestretch_modes = {
    0:  'No stretching or pitch adjustment',
    1:  (
        'Repitch the item, it will become shorter at higher pitches, and '
        'longer at lower pitches'
    ),
    2:  (
        'Stretch the item to the desired length, it will have lower pitch '
        'at longer lengths, and higher pitch at shorter lengths'
    ),
    3:  'Adjust pitch and time independently',
    4: (
        'Same as Rubberband, but preserves formants when pitch shifting.  '
        'Useful on vocal materials, an auto-tune type of pitch shifting'
    ),
    5: (
        'Adjust pitch and time independently, also with the ability to '
        'set start/end pitch/time differently'
    ),
    6:  (
        'Mostly for stretching items very long, creates a very smeared, '
        'atmospheric sound.  Useful for creative reverb-like effects and '
        'soundscapes'
    ),
}


panic = _("""\
The panic button has 2 options:
- Send a note-off event on every note to every plugin, fixes stuck notes
- Stop the audio engine, you will need to restart the application after""")


avconv_error = _(
"""\
Please ensure that ffmpeg (or avconv) and lame are installed.
cannot open mp3 converter dialog.
Check your normal sources for packages or visit:

http://lame.sourceforge.net
http://ffmpeg.org

Cannot find {}""")

export_format = _(
"""File is exported to 32 bit .wav at the sample rate your audio
interface is running at.
You can convert the format using the Menu->Tools dialogs""")

pitchbend_dialog = _("""\
Pitchbend values are in semitones.  Use this dialog to add points with
precision,or double-click on the editor to add points.""")

PianoRollEditor = _("""\
The piano roll editor is used to edit MIDI notes.  See the "Parameter"
combobox, the menu button and the mouse tools in the transport panel.""")


AudioItemSeq = _("""\
Item editor for audio.  Each sequencer item can contain multiple
audio items in addition to MIDI.  Drag audio files from the file browser
onto here.
""")

AudioSeqItem = _("""
A single instance of an audio file.  Right click on an audio item to see the
various tools and actions available.  Select a single item and add effects
using "File FX" and "Item FX" tabs on the right.
"""
)

AUDIO_SEQ_HELP = """\
Select 1+ items, CTRL+click+drag up/down/left/right to copy selected items
Select 1+ items, ALT+SHIFT+Click and drag up/down:
    Modify the volume of the file.  This is useful for mixing, as it modifies
    the volume of every instance of the file in the entire project.
Select 1+ items, CTRL+ALT+Click and drag up/down:
    Modify the volume of selected items.  Different audio items in the
    same sequencer item can have different volumes using this technique.
Select 1+ items, CTRL+SHIFT+Click and drag up/down:
    Create a volume line for the selected items.  For example, you have the
    same kick drum sample repeated 4 times in an item, one beat apart from
    each other.  Select all of them, perform this mouse gesture by clicking
    on the first one and dragging down.  The respective values might be
    -9dB, -6dB, -3dB, 0dB, getting progressively louder.
See the menu button above for additional actions"""

multiple_instances_warning = _("""\
Detected that there are instances of the Stargate audio engine already running.
This could mean that you already have Stargate running, if so you
should click 'Cancel' and close the other instance.

This could also mean that for some reason the engine did not properly
terminate from another session.  If so, click 'OK' to kill the
other process(es)""")

routing_graph = _("""\
Audio (click), sidechain(CTRL+click) and MIDI(SHIFT+click) routing between
tracks. Click below the dest. to route to lower numbered tracks,
above for higher. Double click a track to open plugins
""")

track_panel_dropdown = _("""\
The dropdown menu contains a shortcut to the track plugins (instrument and
effects), and controls for selecting parameters for automation.  For a global
view of track sends, see the routing tab.""")

"""
A track can be any or all of audio, MIDI, send or bus, at the same time.
Instrument plugins can be placed before or after effect plugins, and
will pass-through any audio from items or sends.
"""

