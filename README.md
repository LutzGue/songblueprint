# songblueprint
A Python module that generates songs from chord progressions and song structures based on tonal harmony in twentieth-century music. You can create and practice your own musical compositions by using a machine-readable language that represents the prototype of the song structure. Probabilities are used in a blueprint to determine the chords and the song structure that best suit your style and mood. It's an innovative and creative tool for anyone who loves music and programming.

## parser
- convert manual txt input using tab for hierarchie into nested dictionary
- handle multiple levels of hierarchy
- count the leading spaces (or TAB characters) and determine the indentation level

## Example
### Input (TXT-file)
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
### Example 1
```
["phrase_major_minor"["phrase_major"["meta"["key_major"["f#"]]["meter"["4/4"]]]["song"["predominant"["V"["interval_3k_4k"["interval_3k"["6"]]]]]["start"["T1"["oscil"["type3"["I"["interval_3k"["35"]]]["[viiÂ°]"]["I"["interval_3k"["35"]]]]]]]["conn"["ii"["interval_3k_4k"["interval_3k"["6"]]]]]["end"["cadence"["deceptive_cadence"["V"["cadV"["type1"["V"["46"]]["V"["35"]]]]]["vi"["interval_3k"["35"]]]]]]]]]
```
![example1](https://github.com/LutzGue/songblueprint/blob/main/png/example1.png)
This picture was generated with https://github.com/int2str/jssyntaxtree
### Example 2
```
["phrase_major_minor"["phrase_major"["meta"["key_major"["g"]]["meter"["3/4"]]]["song"["predominant"["none"]]["start"["T1"["SOP"["type2"["I"["interval_3k"["35"]]]["IV"["interval_3k_4k"["interval_4k"["357"]]]]["V"["interval_3k_4k"["interval_4k"["56"]]]]["I"["interval_3k"["46"]]]]]]]["conn"["ii"["interval_3k_4k"["interval_3k"["46"]]]]]["end"["none"]]]]]
```
![example1](https://github.com/LutzGue/songblueprint/blob/main/png/example2.png)
This picture was generated with https://github.com/int2str/jssyntaxtree
