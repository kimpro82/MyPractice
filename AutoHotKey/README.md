# My Auto Hot Key Practice

### \<List>
- [Hello World (2022.09.03)](#hello-world-20220903)
- [Infinity (2021.12.07)](#infinity-20211207)


## [Hello World (2022.09.03)](#list)

- It is so simple but somewhat crazy that `LButton` always calls the message box ……

![Hello World](Images/HelloWorld.PNG)

#### `HelloWorld.ahk`

```ahk
LButton::
    MsgBox, Hello World!

return
```

## [Infinity (2021.12.07)](#list)

- Welcome to `Auto Hot Key` world of mystery!

#### `Infinity.ahk`

```ahk
; Test 1
if (1 == 2)
{
    MsgBox, True
}
else MsgBox, False
```
> False

```ahk
; Test 2
if (11111111111111111111111 == 22222222222222222222222)
{
    MsgBox, True
}
else MsgBox, False
```
> True