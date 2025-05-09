# My-font-library
Font library in Adafruit GFXfont format:
<Adafruit_GFX.h>

## Create your own font header files to work with Adafruit GFX lib. (You can read more details at: learn.adafruit.)
### MANUAL WAY:
- copy your font into directory `GFX_Font_Converter-binary`
- run this in command line (9 means fontsize)
`fontconvert myCoolFont.ttf 9 > myCoolFont9pt7b.h`
- output is your .h file
- following line are needed to work and automatically added at the beginning of each header file:
  ```
    #pragma once
    #include <Adafruit_GFX.h>
  ```

### Batch WAY:
- copy your font into directory `fontsToImport`
- run this in command: `scripts\convertbatch.py`
- it add your fonts .h files in sizes to directory `GFX_Fonts`, if you need more sizes edit table in script `convertbatch.py`
- following line are needed to work and automatically added at the beginning of each header file:
  ```
    #pragma once
    #include <Adafruit_GFX.h>
  ```
- it copies your fontfile (.ttf etc) into `GFX_Fonts/fontname` 
- now move fontfile from `fontsToImport` to `fonts_Imported` and update list in `README.MD`

in Platformio put this header into directory eg: `/lib/myFonts/myCoolFont/`
then in your main.cpp or similar:
`#include <myCoolFont/myCoolFont9pt7b.h>`
and use like:
`tft.setFont(&myCoolFont9pt7b);`

## tested with:
- TFT7735S

## contents:
- 8514fix.fon
- 8514oem.fon
- 8514sys.fon
- AGENCYB.TTF
- AGENCYR.TTF
- Airborne 86.ttf
- ANTQUABI.TTF
- ANTQUAB.TTF
- ANTQUAI.TTF
- ARLRDBD.TTF
- bahnschrift.ttf
- BKANT.TTF
- BRADHITC.TTF
- BRLNSB.TTF
- BRLNSDB.TTF
- BRLNSR.TTF
- BRUSHSCI.TTF
- C64_Pro-STYLE.ttf
- calibrib.ttf
- calibrii.ttf
- calibrili.ttf
- calibril.ttf
- calibriz.ttf
- calibri.ttf
- CascadiaCode.ttf
- CascadiaMono.ttf
- comicbd.ttf
- comici.ttf
- comicz.ttf
- comic.ttf
- COPRGTB.TTF
- COPRGTL.TTF
- corbelb.ttf
- corbeli.ttf
- corbelli.ttf
- corbell.ttf
- corbelz.ttf
- corbel.ttf
- courbd.ttf
- courbi.ttf
- courierstd-boldoblique.otf
- courierstd-bold.otf
- courierstd-oblique.otf
- courierstd.otf
- couri.ttf
- cour.ttf
- covertopscondital.ttf
- covertopscond.ttf
- covertopsexpandital.ttf
- covertopsexpand.ttf
- covertopsital.ttf
- covertops.ttf
- dosapp.fon
- ENGR.TTF
- FREESCPT.TTF
- GOTHICBI.TTF
- GOTHICB.TTF
- GOTHICI.TTF
- GOTHIC.TTF
- HARLOWSI.TTF
- HARNGTON.TTF
- Inkfree.ttf
- ITCBLKAD.TTF
- ITCEDSCR.TTF
- JetBrainsMono-BoldItalic.ttf
- JetBrainsMono-Bold.ttf
- JetBrainsMono-ExtraBoldItalic.ttf
- JetBrainsMono-ExtraBold.ttf
- JetBrainsMono-ExtraLightItalic.ttf
- JetBrainsMono-ExtraLight.ttf
- JetBrainsMono-Italic.ttf
- JetBrainsMono-LightItalic.ttf
- JetBrainsMono-Light.ttf
- JetBrainsMono-MediumItalic.ttf
- JetBrainsMono-Medium.ttf
- JetBrainsMono-Regular.ttf
- JetBrainsMono-ThinItalic.ttf
- JetBrainsMono-Thin.ttf
- KUNSTLER.TTF
- LCALLIG.TTF
- LFAXDI.TTF
- LFAXD.TTF
- LFAXI.TTF
- LFAX.TTF
- LSANSDI.TTF
- LSANSD.TTF
- LSANSI.TTF
- LSANS.TTF
- LTYPEBO.TTF
- LTYPEB.TTF
- LTYPEO.TTF
- LTYPE.TTF
- l_10646.ttf
- N019043l.ttf
- N019044l.ttf
- N019063l.ttf
- N019064l.ttf
- NotoSansJP-Bold.ttf
- NotoSansJP-Regular.ttf
- OCRAEXT.TTF
- OLDENGL.TTF
- PALSCRI.TTF
- PAPYRUS.TTF
- PARCHM.TTF
- PERTIBD.TTF
- PERTILI.TTF
- POORICH.TTF
- PressStart2P.ttf
- PRISTINA.TTF
- Reactor7.ttf
- Roboto-BlackItalic.ttf
- Roboto-Black.ttf
- Roboto-BoldItalic.ttf
- Roboto-Bold.ttf
- Roboto-Italic.ttf
- Roboto-LightItalic.ttf
- Roboto-Light.ttf
- Roboto-MediumItalic.ttf
- Roboto-Medium.ttf
- Roboto-Regular.ttf
- Roboto-ThinItalic.ttf
- Roboto-Thin.ttf
- ROCCB___.TTF
- ROCC____.TTF
- ROCKBI.TTF
- ROCKB.TTF
- ROCKEB.TTF
- ROCKI.TTF
- ROCK.TTF
- seansbd.ttf
- seansbiu.ttf
- seansbi.ttf
- seansbu.ttf
- seansiu.ttf
- seansi.ttf
- seansu.ttf
- seans.ttf
- segoeprb.ttf
- segoepr.ttf
- segoescb.ttf
- segoesc.ttf
- segoeuib.ttf
- segoeuii.ttf
- segoeuil.ttf
- segoeuisl.ttf
- segoeuiz.ttf
- segoeui.ttf
- seguibli.ttf
- seguibl.ttf
- seguiemj.ttf
- seguihis.ttf
- seguili.ttf
- seguisbi.ttf
- seguisb.ttf
- seguisli.ttf
- SEIGDT.TTF
- seisobd.ttf
- seisobiu.ttf
- seisobi.ttf
- seisobu.ttf
- seisoiu.ttf
- seisoi.ttf
- seisou.ttf
- seiso_01.ttf
- seiso_Hungarian.ttf
- seiso.ttf
- SERomand.ttf
- SERomans.ttf
- SESimplex.ttf
- SEStencil.ttf
- Siemens_GOST Type A.ttf
- smalle.fon
- STENCIL.TTF
- swgothe.ttf
- swgothg.ttf
- swgothi.ttf
- swisop1.ttf
- swisop2.ttf
- swisop3.ttf
- swisot1.ttf
- swisot2.ttf
- swisot3.ttf
- swlink.ttf
- swromnd.ttf
- swromns.ttf
- tahomabd.ttf
- tahoma.ttf
- The Old Navy Grunge.ttf
- The Old Navy.ttf
- timesbd.ttf
- timesbi.ttf
- timesi.ttf
- times.ttf
- trebucbd.ttf
- trebucbi.ttf
- trebucit.ttf
- trebuc.ttf
- verdanab.ttf
- verdanai.ttf
- verdanaz.ttf
- verdana.ttf
- vgaoem.fon
- VINERITC.TTF
- VIPER__.TTF
- VIVALDII.TTF
- VLADIMIR.TTF
- webdings.ttf
- wingding.ttf
- WINGDNG2.TTF
- WINGDNG3.TTF
