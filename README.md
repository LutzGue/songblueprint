# songblueprint -- music composition with Python
A Python module that generates songs from chord progressions and song structures based on tonal harmony in twentieth-century music. You can create and practice your own musical compositions by using a machine-readable language that represents the prototype of the song structure. Probabilities are used in a blueprint to determine the chords and the song structure that best suit your style and mood. It's an innovative and creative tool for anyone who loves music and programming.

## parser
- convert manual txt input using tab for hierarchie into nested dictionary
- handle multiple levels of hierarchy
- count the leading spaces (or TAB characters) and determine the indentation level

## Examples
### Input (TXT-file)
This tool is similar to a musical dice game that Mozart once developed: It generates a new phase of music. There are numerous sources that describe how musical phrases can be constructed in an interesting and functionally solid way. This science has been very well researched over many hundreds of years. The problem is to make this rule set machine readable (because example sheets are presented as images and not in text format) and the user should need minimal typing effort to convert it into machine readable format.

![example1](https://github.com/LutzGue/songblueprint/blob/main/img/music_theory_book_convert_parsing_tree.jpg)

Now, it's super easy to edit: Just open the notepad and bring it into a simple structure, write it down quickly and add some propabilities comma separated like in this example:
```
cadV
    cadV_type1, 10
        V
            46
        V
            35
    cadV_type2, 10
        V
            46
        V
            357
```
You can also save yourself typing effort and use variables in curly brackets instead, to replace the text directly, as shown in this example:
```
interval_3k
    35,10
    6,10
    46,10
interval_4k
    357,10
    56,10
    34,10
    2,10
interval_3k_4k
    {interval_3k},10
    {interval_4k},10
```
### Result (nested dictionary in py)
```
{
    'cadV': {
        'cadV_type1': {
            'value': '10',
            'V46': {},
            'V35': {}
        },
        'cadV_type2': {
            'value': '10',
            'V46': {},
            'V357': {}
        }
    }
}
```
## Generated parsing trees
Based on the defined probability distribution, a parsing tree syntax is created, which can be displayed graphically. The parsing tree contains all layers from the "background", "middleground" and "foreground" (Schenker), so that in the end the original plan is still transparent as the backbone and is preserved. This graphical presentation allows all levels to remain in parallel in the focus of the musical analysis.

![example1](https://github.com/LutzGue/songblueprint/blob/main/img/dices_music_sheet.jpg)

### Example 1
```
["phrase_major_minor"["phrase_major"["meta"["key_major"["f#"]]["meter"["4/4"]]]["song"["predominant"["V"["interval_3k_4k"["interval_3k"["6"]]]]]["start"["T1"["oscil"["type3"["I"["interval_3k"["35"]]]["[viiÂ°]"]["I"["interval_3k"["35"]]]]]]]["conn"["ii"["interval_3k_4k"["interval_3k"["6"]]]]]["end"["cadence"["deceptive_cadence"["V"["cadV"["type1"["V"["46"]]["V"["35"]]]]]["vi"["interval_3k"["35"]]]]]]]]]
```
![example1](https://github.com/LutzGue/songblueprint/blob/main/img/example1.png)
This picture was generated with https://github.com/int2str/jssyntaxtree
### Example 2
```
["phrase_major_minor"["phrase_major"["meta"["key_major"["g"]]["meter"["3/4"]]]["song"["predominant"["none"]]["start"["T1"["SOP"["type2"["I"["interval_3k"["35"]]]["IV"["interval_3k_4k"["interval_4k"["357"]]]]["V"["interval_3k_4k"["interval_4k"["56"]]]]["I"["interval_3k"["46"]]]]]]]["conn"["ii"["interval_3k_4k"["interval_3k"["46"]]]]]["end"["none"]]]]]
```
![example1](https://github.com/LutzGue/songblueprint/blob/main/img/example2.png)
This picture was generated with https://github.com/int2str/jssyntaxtree
# Next Steps:
1) integration Analyzing Levels (background, middleground); edit in txt: show/hide L1, L2, roman numeral is always visible
2) create MIDI file using music21 (roman numeral to key) --> melody harmonization: provide 3-4 possible melody notes based on the generated patterns
3) remove probability and total calculation
4) generate batch job --> generate multiple JSON-output-files suffix timestamp
5) edit in txt: replicate function (min/max value of replications in TXT)
6) merge all functions 01-06
7) py command line (parameters: file input, file out, commands: midi/no.of generations/PNG export/melody match/...)
8) generate training data for ML: adding labels for training data
9) create more music-phrase.txt files

## Inspirational Tool
The common way of creating chord progressions is to fill 4 bars with 4 bass notes, then fill them with chords from the scale in the key and loop. This helps create driving grooves and inspiring moods. But it is not a phrase, it has no overarching functional connection. Therefore, this article explains how to use phrases with cadences to tell longer self-contained satisfying stories and avoid endless loops that make melody development difficult and shift the focus away from the groove.

This tool is also an inspirational tool: You can use the generated phrase as a starting point for your melody development. You can add the generated Roman Numeral Progression in the online tool “Automatic SATB Part-Writer” and choose the most melodic one from the different positions (voicings) in keyboard style or in four-part-writing style. Then you can fill in the transitions with passing notes in the roll editor of your DAW (Digital Audio Workstation). You can also practice the piece with feeling on the instrument and record it.

Here are some examples of how you can use this tool to create your own songs:

Example 1: keyboard voicing in the key of C# Minor
![example1](https://github.com/LutzGue/songblueprint/blob/main/img/keyboard_style_example1.jpg)
This sheet was generated with "Automatic SATB Part-Writer", https://partwriter.com/

Example 2: four part writing voicing in the key of C# Minor
![example2](https://github.com/LutzGue/songblueprint/blob/main/img/four_part_writing_example2.jpg)
This sheet was generated with "Automatic SATB Part-Writer", https://partwriter.com/

Example 3: Highlight melodic line in outline voices. The most important voices are Sopran and Bass. In the example below a leap between the 4th and 5th sopran note marks the focal point (highest note). Trace the shape of the voices (arc / line) and identify the motion type (parallel / oblique / contrary).
![example3](https://github.com/LutzGue/songblueprint/blob/main/img/melody_line_example_1.PNG)

Example 4: Interesting moving up bass line.
![example6](https://github.com/LutzGue/songblueprint/blob/main/img/daw_satb_example2.PNG)

Example 5: Easy to play four part writing on piano. The intervals in both the right and left hands are limited to the circumference of an octave and can therefore be practiced comfortably.
![example6](https://github.com/LutzGue/songblueprint/blob/main/img/four_part_writing_example2.PNG)

Example 6: Practice the piece on the instrument yourself. This will make you more flexible in dealing with unfamiliar keys and develop a feeling in your fingers. This autonomy will allow you to improvise later and have fun.
![example4](https://github.com/LutzGue/songblueprint/blob/main/img/practicing_example_1.PNG)
Screenshot, "Syntthesia", https://www.synthesiagame.com/

Example 7: Coloring voices and scales in DAW Roll Editor. This is for preparing the next step ((adding passing notes / embelishing). The alto and tenor voices should have as little movement as possible and have a line that is as linear as possible.
![example5](https://github.com/LutzGue/songblueprint/blob/main/img/daw_satb_example1.PNG)

Example 8: Adding some passing, sustain, retardation, auxilary / neighbour tones, bass lines as "Highlights" and embellishment into the voices. Develop an interesting melodic Bass line as independent counterpoint to the melody in the sopran voice.
![example6](https://github.com/LutzGue/songblueprint/blob/main/img/daw_satb_highlights_example1.PNG)

Example 9: In four part voicing, the individual colored voices can be easily divided into different instruments and thus fill different frequency spectra without overlaying them. As a result, we want to have the widest possible frequency image in the mix with a lot of texture in the sound and avoid a muddy sound. The individual voices can be placed in the stereo image.
![example6](https://github.com/LutzGue/songblueprint/blob/main/img/split_SATB_voices_into_stereo_and_frequency.jpg)

Example 10: To create a harmonious melody, you can slow down the tempo (e.g. halve it) and use the soprano voice as structural notes. These structural notes serve as a basis to play around and fill out with new notes as decorations. To achieve this, one can use modal scales, such as Ionian for I and Dorian for ii, which correspond to specific harmonic functions. Similar to the gravitational pull of the Sun around celestial bodies, the structural note has an inherent gravitational pull that influences the surrounding notes in the musical universe. 
To leave the current universe you can fly to the next structural universe: Suitable transition tones are then found for the following structural note in the soprano voice. This process is repeated in the next “structural note universe”.
Analogous to a symphony of the cosmos, the sun acts as a structural note around which the earth and moon rotate, similar to notes on a musical scale. Just as gravity binds the Earth and the Moon to the Sun, all notes are connected to the structural note within their universe. Together they form a harmonious structure or “sound space”, similar to the solar system, which consists of the sun, earth and moon. The Sun's gravitational force holds the planets in their orbits, making them the stable and central point in this cosmic composition.
![example6](https://github.com/LutzGue/songblueprint/blob/main/img/structural_note_universes.jpg)

Example 11: Develop variations on the melody in the Soprano voice and extend the phrase by combining them. Make dynamic choices: start simple and build up dynamic.