# My Basic Practice

My Nostalgia; codes for **the old BASIC product family** (*GW-BASIC*, *QuickBASIC* and so on) before [*Visual Basic*](../VBA)


### \<List>

- [Line Numbering (2023.07.19)](#line-numbering-20230719)
- [Draw A Car (2022.02.09)](#draw-a-car-20220209)
- [Play Music (2021.02.20)](#play-music-20210220)
- [Hello World (2020.02.27)](#hello-world-20200227)


## [Line Numbering (2023.07.19)](#list)

- I intended to write *GW-BASIC* code, but I actually executed it in *QuickBASIC*.
- However, since it is a superset, it seems to be fine.

  <details open="">
    <summary>Codes : LineNum.bas</summary>

  ```bas
  '-10 print "-10"        ' A negative line number causes an error
  0 CLS
  10 PRINT "10"
  15 GOTO 30
  20 PRINT "20"           ' Pass
  30 PRINT "30"
  30.5 PRINT "30.5"       ' Decimal point is available
  65535 PRINT "65535"
  65536 PRINT "65536"     ' The line number can be over 65536
  ```
  ```txt
  10
  30
  30.5
  65535
  65536
  ```
  </details>


## [Draw A Car (2022.02.09)](#list)

- Remember how I felt when I was a primary school student

  ![Draw A Car](Images/QB_DrawingCar.PNG)

  <details>
    <summary>Codes : DrawCar.bas</summary>

  ```bas
  CLS

  SCREEN 12       '640 x 480 / 16 colors
  wid% = 640      'Can I get these parameters automatically?
  hei% = 480

  'Border
  LINE (10, 10)-(wid% - 10, 10), 15, B
  LINE (10, hei% - 80)-(wid% - 10, hei% - 80), 15, B
  LINE (10, 10)-(10, hei% - 80), 15, B
  LINE (wid% - 10, 10)-(wid% - 10, hei% - 80), 15, B

  'Memo
  LOCATE 3, 5
  PRINT "QuickBasic : My Nostalgia"
  LOCATE 3, 67
  PRINT "2022.02.09"

  'Body
  LINE (wid% / 2 - 100, hei% / 2 - 100)-(wid% / 2 + 100, hei% / 2), 7, BF
  LINE (wid% / 2 - 200, hei% / 2)-(wid% / 2 + 200, hei% / 2 + 100), 7, BF

  'Windows
  LINE (wid% / 2 - 100, hei% / 2 - 80)-(wid% / 2 - 60, hei% / 2), 9, BF
  LINE (wid% / 2 - 50, hei% / 2 - 80)-(wid% / 2 - 5, hei% / 2), 9, BF
  LINE (wid% / 2 + 5, hei% / 2 - 80)-(wid% / 2 + 50, hei% / 2), 9, BF
  LINE (wid% / 2 + 60, hei% / 2 - 80)-(wid% / 2 + 100, hei% / 2), 9, BF

  'Wheels
  CIRCLE (wid% / 2 - 90, hei% / 2 + 100), 50, 8
  CIRCLE (wid% / 2 + 90, hei% / 2 + 100), 50, 8
  PAINT (wid% / 2 - 120, hei% / 2 + 100), 8, 8
  PAINT (wid% / 2 + 120, hei% / 2 + 100), 8, 8
  CIRCLE (wid% / 2 - 90, hei% / 2 + 100), 30, 7
  CIRCLE (wid% / 2 + 90, hei% / 2 + 100), 30, 7
  PAINT (wid% / 2 - 90, hei% / 2 + 100), 7, 7
  PAINT (wid% / 2 + 90, hei% / 2 + 100), 7, 7

  END
  ```
  </details>


## [Play Music (2021.02.20)](#list)

- Practice of functions : `BEEP` `SOUND` `PLAY`
- Run by *MS QuickBASIC 4.5*

  <details>
    <summary>Codes : Xerxes.bas</summary>

  - Using `SHELL` function to borrow the `CLS` command from DOS
  ```bas
  SHELL "CLS"
  PRINT "I am generous"
  ```
  > I am generous
  </details>
  <details>
    <summary>Codes : Sound.bas</summary>

  - Refer to ☞ https://en.wikibooks.org/wiki/QBasic/Sound
  ```bas
  SHELL "CLS"

  'BEEP
  PRINT "BEEP"
  BEEP
  PRINT CHR$(7)
  SLEEP

  'SOUND
  PRINT "SOUND" + CHR$(13) 'CHR$(13) : Line break
  FOR i% = 1 TO 30
          SOUND i% * 100, 1  'Frequency, Duration
  NEXT
  SLEEP

  'PLAY
  PRINT "PLAY" + CHR$(13)
  PLAY "L16 CDEFGAB>C" '> : Move up one octave
  SLEEP
  ```
  </details>

  - **Results** : [BEEP](./Sounds/QB_SOUND_BEEP.wav) [SOUND](./Sounds/QB_SOUND_SOUND.wav) [PLAY](./Sounds/QB_SOUND_PLAY.wav)  
  (* These can't be played directly, but played after downloading.)

  <details open="">
    <summary>Codes : SchoolBell.bas</summary>

  - Play the same song with the keys of both C major and C minor
  ```bas
  SHELL "CLS"

  PRINT "School Bell"

  PRINT "C major"
  PLAY "MS G8G8A8A8 G8G8E4 G8G8E8E8 D6 P8"
  PLAY "MS G8G8A8A8 G8G8E4 G8E8D8E8 C6 P8"

  PRINT "C minor"
  PLAY "MS G8G8A-8A-8 G8G8E-4 G8G8E-8E-8 D6 P8"
  PLAY "MS G8G8A-8A-8 G8G8E-4 G8E-8D8E-8 C6 P8"
  ```
  </details>

  - **Results** : [C major](./Sounds/QB_PLAY_C%20major.wav) [C minor](./Sounds/QB_PLAY_C%20minor.wav)  
  (* These can't be played directly, but played after downloading.)


## [Hello World (2020.02.27)](#list)

- `PRINT`, not `print`

  <details>
    <summary>Codes : HelloWorld.bas</summary>

  ```bas
  print "Hello World!"
  ```
  > Call to undefined sub 'print'

  ```bas
  print("Hello World!")
  ```
  > Call to undefined sub 'print'

  ```bas
  print 'Hello World!'
  ```
  > Call to undefined sub 'print'

  How can I make `print` work?

  ```bas
  PRINT "Hello World!"
  ```
  > Hello World!

  The secret was UPPER CASE!

  ```bas
  PRINT 'Hello World!'
  ```
  >
  `''` seems to be used for single-line comments.

  ```bas
  'You can't see what I'm saying.'
  ```
  ㅋ
  </details>