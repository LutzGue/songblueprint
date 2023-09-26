# songblueprint
A Python module that generates songs from chord progressions and song structures based on tonal harmony in twentieth-century music. You can create and practice your own musical compositions by using a machine-readable language that represents the prototype of the song structure. Probabilities are used in a blueprint to determine the chords and the song structure that best suit your style and mood. It's an innovative and creative tool for anyone who loves music and programming.

## parser
- convert manual txt input using tab for hierarchie into nested dictionary
- handle multiple levels of hierarchy
- count the leading spaces (or TAB characters) and determine the indentation level

## Examples
### Input (TXT-file)
It's super easy to edit. Just open the notepad and bring it into a simple structure, write it down quickly and add some propabilities comma separated like in this example:
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
You can also save yourself typing effort and use variables in curly brackets instead to replace the text directly, as shown in this example:
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
Based on the defined probability distribution, a parsing tree syntax is created, which can be displayed graphically.
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

### Inspirational Tool
Use it as an inspiration tool: Add the generated Roman Numeral Progresson in the online tool "Automatic SATB Part-Writer" and choose the most melodic one from the different positions in keyboard style or in 4-part-writing style. Then fill in the transitions with passing notes in the roll editor of your DAW. Übe das Stück mit Gefühl auf dem Instrument.
![example1](https://github.com/LutzGue/songblueprint/blob/main/img/keyboard_style_example1.jpg)
This sheet was generated with "Automatic SATB Part-Writer", https://partwriter.com/
![example1](https://github.com/LutzGue/songblueprint/blob/main/img/four_part_writing_example2.jpg)
This sheet was generated with "Automatic SATB Part-Writer", https://partwriter.com/