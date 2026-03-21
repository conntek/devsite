# KTH4603 - 完整技术参考

[返回产品目录](/products/) | [返回KTH46xx系列](/products/KTH46xx/)


## 🧭 页面导航

- 🔙 [返回产品摘要页面](/products/KTH46xx/KTH4603)
- 📂 [返回KTH46xx系列](/products/KTH46xx/)
- 🏠 [返回主页](/)
- 📚 [所有增强版技术参考](./index.md)

---

## 产品概述

**KTH4603** 完整技术参考文档，包含所有PDF数据手册的详细内容和技术图片。

---

## 产品图片

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

**产品图片**
*产品图片请参考产品数据手册*

---

## 📄 KTH4603 Datasheet_EN.pdf

<details>
<summary>点击展开 KTH4603 Datasheet_EN.pdf 完整内容</summary>

# KTH4603 Series

## Ultra-Low Power, High-Sensitivity 3D Hall Switch

### Technical Support sales.global@conntek.com.cn

#### 2024- 8- 21


#### Disclaimer

The information in this document is provided by Quanzhou KTsense Microelectronics Co., Ltd. (泉州昆
泰芯微电子科技有限公司) (hereafter referred to as ”KTsense Micro”) on an ”as is” basis for informational
purposes only. KTsense Micro does not guarantee the accuracy of the information contained herein or
the outcomes of its implementation. KTsense Micro assumes no liability for any errors or inaccuracies
that may be present in this document. Users assume full responsibility for the application of the practices
outlined in this document.


KTsense Micro owns the registered trademark CONNTEK, under which the CONNTEK brand sensors are
marketed.


This document comes without any warranties, express or implied, including but not limited to warranties
of merchantability, satisfactory quality, non-infringement, and fitness for a particular purpose. KTsense
Micro, along with its employees, agents, and affiliates, is not liable for any losses arising from the use or
reliance on this document.


This document is subject to change without prior notice and should not be construed as a commitment
by KTsense Micro. Users should ensure they have the latest version of the relevant information before
placing orders or integrating the product into their systems.


Users must evaluate the suitability of the product described in this document for their specific applications, including the required level of reliability and fitness for purpose.


This document and the described product may be subject to export control regulations. Export may require prior authorization from the competent authorities. The product is not intended, authorized, or warranted for use in applications requiring extended temperature ranges or unusual environmental conditions. High reliability applications, such as medical life-support or aviation systems, are specifically excluded.


The product may not be used for the development, production, maintenance, or storage of:


1. Chemical, biological, or nuclear weapons, including missile systems for such weapons.
2. Civil firearms, including spare parts or ammunition.
3. Defense-related products or materials for military or law enforcement use.

4. Applications that could cause serious harm to persons or property and that can be used as a means
of violence in armed conflicts or similar situations.


No licenses or rights to any intellectual property of KTsense Micro or third parties are granted.


If this document is marked as “confidential”or similar, or if the content is reasonably understood to be
confidential, the recipient must not disclose any part of the document to third parties without the express
written consent of KTsense Micro. The recipient must take all necessary measures to maintain the confidentiality of the document, using at least the same degree of care as they use to protect their own confidential information, but no less than a reasonable degree of care. The recipient may only disclose the
document to employees on a need-to-know basis, provided they are bound by confidentiality terms similar to those in this disclaimer. The document may only be used for the purpose for which it was received
and may not be used for commercial purposes or to the detriment of KTsense Micro or its customers.
These confidentiality obligations will last indefinitely but in any case, for no less than 10 years from the
receipt of the document.


This disclaimer is governed by the laws of China, and any disputes arising from it will be subject to the
exclusive jurisdiction of the courts in Shenzhen, China.


The invalidity of any provision in this disclaimer does not affect the validity of the remaining provisions.
Previous versions of this document are repealed.


KTH4603 Series

#### Copyright


This document and its contents are protected by copyright law. No part of this document may be reproduced or distributed in any form or manner without the prior written consent of KTsense Micro.

#### Contact Information


[For the latest version of this document, go to our website at https://en.conntek.com.cn/.](https://en.conntek.com.cn/)


For additional information, please contact our Direct Sales team and get help for your specific needs:

|Region|Contact Information|
|---|---|
|Overseas|Email: sales.global@conntek.com.cn|
|China|Email: sales@conntek.com.cn|



3 of 18


## Table of Contents

**1 Product Features** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **5**


**2 Typical Applications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **5**


**3 Overview** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **5**


**4 Pin Definitions and Marking Information** . . . . . . . . . . . . . . . . . . . . . . . **7**


**4.1** SOT-23-3L . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

**4.2** SOT-23-6L . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


**5 Functional Block Diagram** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **8**


**6 Output Characteristics** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **8**


**7 Product Model Name Structure** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **9**


**8 Absolute Maximum Ratings** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **9**


**9 Operating Conditions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **10**


**10 Electrical Parameters** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **10**


**11 Magnetic Parameters** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **12**


**12 Performance Curves** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **13**


**13 Ordering Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **15**


**14 Typical Applications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **16**


**15 Package Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **17**


**15.1** SOT-23-3L Package Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
**15.2** SOT-23-6L Package Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


KTH4603 Series

## 1 Product Features

### • [Low Power Consumption] –

[2.5 Hz version:][ 4] _[.]_ [5] _[ µA]_ [ @][ 2] _[.]_ [5] _[ V]_

### –

[5.0 Hz version:][ 7] _[.]_ [1] _[ µA]_ [ @][ 2] _[.]_ [5] _[ V]_

### • [Wide Operating Voltage Range:][ 2] [.] [5] [ V][ ∼] [5] [.] [5] [ V] • [Magnetic Field Threshold (B] OP [):][ 25][ Gs] • [Omnipolar Magnetic Field Detection] • [NMOS Open-Drain Output] • [Package: SOT-23-3L, SOT-23-6L] • [Operating Temperature Range:] [ −] [40] [ ◦] [C] [ ∼] [125] [ ◦] [C] • [Superior ESD Performance: HBM][ 6][ kV] • [RoHS Compliant]

## 2 Typical Applications

### • [3D Magnetic Field Switch Detection] • [Anti-Tampering Detection for Meters (Electricity/Wa-]

ter/Gas)

### • [Intelligent Door and Window Detection] • [Electric Garage Door Detection]

## 3 Overview


The KTH4603 series is a low-power Hall effect switch sensor with 3D omnipolar detection. The chip offers multiple
switching frequencies and packaging options to suit various
applications.


When the applied south or north magnetic flux density exceeds the operating point (B OP ), the chip outputs a low level
and maintains it until the flux density drops below the release point (B RP ). The chip incorporates X, Y, Z ultra-sensitive
low-offset Hall plates, multiplexer analog switches, differential amplifiers, Schmitt triggers, and NMOS open-drain output circuits. Advanced SPIN and digital filtering technology,
as well as optimized clock control technology, ensure stable
operating points and switching frequencies.


5 of 18


KTH4603 Series


The KTH4603 series operates within a supply voltage range
of 2 _._ 5 _V_ to 5 _._ 5 _V_ and is available in standard SOT-23-3L and
SOT-23-6L packages.


Figure 1: SOT-23-3L


Figure 2: SOT-23-6L


6 of 18


KTH4603 Series

## 4 Pin Definitions and Marking Information

#### 4.1 SOT-23-3L


Figure 3: SOT-23-3L Pinout Top View

|Pin Name|Pin Number|Function Description|
|---|---|---|
|VDD<br>OUT<br>GND|1<br>2<br>3|Power Supply Input<br>Output<br>Ground|


#### 4.2 SOT-23-6L


Figure 4: SOT-23-6L Pinout Top View


7 of 18


KTH4603 Series

|Pin Name|Pin Number|Function Description|
|---|---|---|
|VDD<br>TEST<br>OUTX<br>OUTY<br>GND<br>OUTZ|1<br>2<br>3<br>4<br>5<br>6|Power Supply Input<br>Ground<br>X-Axis Output<br>Y-Axis Output<br>Ground<br>Z-Axis Output|


## 5 Functional Block Diagram


Figure 5: Functional Block Diagram

## 6 Output Characteristics


For the single output option of KTH4603XX-ST3, when a
magnetic field perpendicular to any of the Hall sensors (X,
Y, or Z direction) exceeds the B OPS (or falls below B OPN ), the
chip outputs a low level (switch closed). The KTH4603XXST6 has three separate outputs (X, Y, or Z). When a magnetic field is applied to the Hall chip, and the magnetic flux
density in the corresponding direction exceeds the operating point B OPS (or falls below B OPN ), the corresponding output pin outputs a low level (switch closed). When the magnetic flux density drops below the release point B RPS (or rises
above B RPN ), the corresponding output pin outputs a high
level (switch open). The difference between the operating
point and release point flux density is the hysteresis (B HY ).
This built-in hysteresis ensures stable output unaffected by
mechanical vibration and magnetic noise. When powered
on, if the magnetic flux density is between B OP and B RP, the


8 of 18


KTH4603 Series


output is in an indeterminate state. The confirmed output
state is determined by the first magnetic field that exceeds
B OP or B RP .


Figure 6: Output Characteristics

## 7 Product Model Name Structure

## 8 Absolute Maximum Ratings


T A =25 _[◦]_ C (unless otherwise specified) All voltages are referenced to GND.


9 of 18


KTH4603 Series

|Item|Parameter Description|Min|Max|Unit|
|---|---|---|---|---|
|VDD<br>IOUTPUT<br>B<br>TSTG<br>TJ<br>ESD|Supply Voltage<br>Output Drive Current<br>Magnetic Flux Density<br>Storage Temperature Range<br>Junction Maximum Temperature<br>HBM ESD Capability|-0.3<br>-<br>No Limit<br>-50<br>-<br>-6000|6<br>30<br>-<br>150<br>150<br>6000|V<br>mA<br>Gs<br>_◦_C<br>_◦_C<br>V|



Note: Exceeding the absolute maximum ratings may cause
permanent damage. Prolonged operation at the absolute
maximum ratings may affect the reliability of the chip.

## 9 Operating Conditions


T A = 25 _[◦]_ C (unless otherwise specified)

|Item|Parameter Description|Operating Condition|Value|Unit|
|---|---|---|---|---|
|VDD<br>TA|Supply Voltage Range<br>Operating Temperature Range|Operating Voltage<br>Operating Temperature|2_._5_ ∼_5_._5<br>_−_40_ ∼_125|V<br>_◦_C|


## 10 Electrical Parameters


T A =25 _[◦]_ C, V DD =3 _._ 3 _V_ (unless otherwise specified)


10 of 18


KTH4603 Series





















|Parameter<br>Symbol|Parameter<br>Description|Test Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD|Supply Voltage|-|2_._5|3_._3|5_._5|V|
|IDD|Wake-Up<br>Current|VDD=2_._5_ V_, TA=25 _◦_C|-|2_._7|-|mA|
||Sleep Current|VDD=2_._5_ V_, TA=25 _◦_C|-|2_._5|-|_µ_A|
||Average<br>Current<br>(KTH4603AA)|VDD=2_._5_ V_, TA=25 _◦_C|-|4_._5|-|_µ_A|
||Average<br>Current<br>(KTH4603AA)|VDD=5_._0_ V_, TA=25 _◦_C|-|6|-|_µ_A|
||Average<br>Current<br>(KTH4603AB)|VDD=2_._5_ V_, TA=25 _◦_C|-|7_._1|-|_µ_A|
||Average<br>Current<br>(KTH4603AB)|VDD=5_._0_ V_, TA=25 _◦_C|-|9|-|_µ_A|
|IOUTOFF|Output<br>Leakage<br>Current|_|B| < |B_RP_|_|-|-|10|_µ_A|
|VOUT|Output Voltage|IOUT=2 mA, B>BOP|-|20|-|mV|
|TAWAKE|Wake-Up Time||-|405|-|_µ_s|
|TPERIOD|Period|KTH4603AA Series|-|408|-|ms|
|||KTH4603AB Series|-|205|-|ms|


Note: To maintain the chip’s low average power consumption, the internal sampling circuit periodically switches between Awake and Sleep states. Each axis of the sensor is
powered on for 135 _µ_ s before entering a low-power Sleep
mode. This Awake and Sleep cycle occurs three times in
each period, allowing the X, Y, and Z axes to be sampled
during their respective cycles. During the brief Awake time,
the chip samples and holds the magnetic field data, outputs
the corresponding result, and locks the data at the end of
each cycle. During each Sleep cycle, the output state remains in the current determined state, and the high/low output level does not affect the chip’s operating current.


11 of 18


KTH4603 Series

## 11 Magnetic Parameters


T A =25 _[◦]_ C, V DD =3 _._ 3 _V_ (unless otherwise specified)















|Parameter<br>Symbol|Parameter<br>Description|Test Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|BOPS|Operating<br>Point (South<br>Pole)|South pole to the<br>left, bottom or side<br>with printed<br>markings. Refer to<br>Figure 7|-|25|40|Gs|
|BOPN|Operating<br>Point (North<br>Pole)|North pole to the<br>left, bottom or side<br>with printed<br>markings. Refer to<br>Figure 7|_−_40|_−_25|-|Gs|
|BRPS|Release<br>Point (South<br>Pole)|South pole to the<br>left, bottom or side<br>with printed<br>markings. Refer to<br>Figure 7|5|15|-|Gs|
|BRPN|Release<br>Point (North<br>Pole)|North pole to the<br>left, bottom or side<br>with printed<br>markings. Refer to<br>Figure 7|-|_−_15|_−_5|Gs|
|BHY|Hysteresis|BHY=|BOP - BRP||-|10|-|Gs|


12 of 18


KTH4603 Series


Figure 7: Three-Dimensional Magnetic Field Orientation

## 12 Performance Curves



Figure 8: Average Power
Consumption VS Supply Voltage
@TA=25 _[◦]_ C


Figure 10: Low Output Voltage
VS Supply Voltage @TA=25 _[◦]_ C,
_I_ _OUT_ = 20 _mA_



Figure 9: Average Power
Consumption VS Operating
Temperature @VDD=3.3V


Figure 11: Low Output Voltage
VS Operating Temperature
@VDD=3.3V, _I_ _OUT_ = 20 _mA_


13 of 18


KTH4603 Series


Figure 12: Operating Period VS
Supply Voltage @TA=25 _[◦]_ C


Figure 14: X-Axis Magnetic
Threshold VS Supply Voltage
@TA=25 _[◦]_ C


Figure 16: Y-Axis Magnetic
Threshold VS Supply Voltage
@TA=25 _[◦]_ C


Figure 18: Z-Axis Magnetic
Threshold VS Supply Voltage
@TA=25 _[◦]_ C



Figure 13: Operating Period VS
Operating Temperature
@VDD=3.3V


Figure 15: X-Axis Magnetic
Threshold VS Operating
Temperature @VDD=3.3V


Figure 17: Y-Axis Magnetic
Threshold VS Operating
Temperature @VDD=3.3V


Figure 19: Z-Axis Magnetic
Threshold VS Operating
Temperature @VDD=3.3V


14 of 18


KTH4603 Series


Figure 20: X-Axis Magnetic
Hysteresis VS Supply Voltage
@TA=25 _[◦]_ C


Figure 22: Y-Axis Magnetic
Hysteresis VS Supply Voltage
@TA=25 _[◦]_ C


Figure 24: Z-Axis Magnetic
Hysteresis VS Supply Voltage
@TA=25 _[◦]_ C



Figure 21: X-Axis Magnetic
Hysteresis VS Operating
Temperature @VDD=3.3V


Figure 23: Y-Axis Magnetic
Hysteresis VS Operating
Temperature @VDD=3.3V


Figure 25: Z-Axis Magnetic
Hysteresis VS Operating
Temperature @VDD=3.3V


## 13 Ordering Information

|Model|Package<br>Type|Number<br>of Pins<br>of|Magnetic<br>Threshold<br>(B )<br>OP|Switching<br>Frequency|Temperature|
|---|---|---|---|---|---|
|KTH4603AA-ST3|SOT-23-3L|3|25Gauss|2.5Hz|_−_40_◦_C_ ∼_125_◦_C|
|KTH4603AB-ST3|SOT-23-3L|3|25Gauss|5Hz|_−_40_◦_C_ ∼_125_◦_C|
|KTH4603AA-ST6|SOT-23-6L|6|25Gauss|2.5Hz|_−_40_◦_C_ ∼_125_◦_C|
|KTH4603AB-ST6|SOT-23-6L|6|25Gauss|5Hz|_−_40_◦_C_ ∼_125_◦_C|



15 of 18


KTH4603 Series

## 14 Typical Applications


The KTH4603XX operates within an input voltage range of
2 _._ 5 _V_ to 5 _._ 5 _V_ . To filter noise at the chip’s power terminal, a
filtering capacitor between the power supply and ground is
recommended. This capacitor should be 1 _µF_ and placed
as close to the VDD pin as possible. Typically, the use of a
PCB copper layer below the KTH4603XX device does not affect the magnetic flux density or interfere with the device’s
performance since copper is not ferromagnetic. However, if
nearby system components contain iron or nickel, they may
unpredictably alter the magnetic flux density.


Figure 26: Typical Application of KTH4603XX-ST3


Figure 27: Typical Application of KTH4603XX-ST6


16 of 18


KTH4603 Series

## 15 Package Information

#### 15.1 SOT-23-3L Package Information


Figure 28: Package dimension of SOT-23-3L

|Symbol|Min (mm)|Typ (mm)|Max (mm)|
|---|---|---|---|
|A<br>A1<br>A2<br>b<br>c<br>D<br>E<br>E1<br>e<br>e1<br>L<br>_θ_|-<br>0_._00<br>1_._00<br>0_._30<br>0_._10<br>2_._82<br>2_._65<br>1_._50<br>0_._85<br>1_._80<br>0_._30<br>0_◦_|-<br>-<br>1_._10<br>-<br>-<br>2_._95<br>2_._80<br>1_._65<br>0_._95<br>1_._90<br>0_._45<br>-|1_._25<br>0_._1<br>1_._15<br>0_._50<br>0_._20<br>3_._02<br>2_._95<br>1_._70<br>1_._05<br>2_._00<br>0_._60<br>8_◦_|



17 of 18


KTH4603 Series

#### 15.2 SOT-23-6L Package Information


Figure 29: Package dimension of SOT-23-6L

|Symbol|Dimensions In Millimeters<br>Min Max|Dimensions In Inches<br>Min Max|
|---|---|---|
|A<br>A1<br>A2<br>b<br>c<br>D<br>E1<br>E<br>e<br>e1<br>L<br>L1<br>_θ_|1_._050<br>1_._280<br>0_._000<br>0_._130<br>1_._050<br>1_._150<br>0_._300<br>0_._500<br>0_._100<br>0_._200<br>2_._820<br>3_._020<br>1_._500<br>1_._720<br>2_._650<br>3_._000<br>0_._950 (BSC)<br>1_._800<br>2_._000<br>0_._300<br>0_._600<br>0_._600 (REF)<br>0_◦_<br>8_◦_|0_._041<br>0_._050<br>0_._000<br>0_._005<br>0_._041<br>0_._045<br>0_._012<br>0_._020<br>0_._004<br>0_._008<br>0_._111<br>0_._119<br>0_._059<br>0_._068<br>0_._104<br>0_._118<br>0_._037 (BSC)<br>0_._071<br>0_._079<br>0_._012<br>0_._024<br>0_._024 (REF)<br>0_◦_<br>8_◦_|



18 of 18




</details>

---

## 📄 KTH4603XX产品手册V1.0.pdf

<details>
<summary>点击展开 KTH4603XX产品手册V1.0.pdf 完整内容</summary>

 低功耗


  - 2.5Hz版本：4.5uA@2.5V


  - 5.0Hz版本：7.1uA@2.5V


 宽工作电压范围：2.5V~5.5V


 磁场阈值（Bop）


   - 25Gs 阈值


 全极磁场检测


 NMOS开漏输出


 封装：SOT-23-3L，SOT-23-6L


 工作温度范围：-40℃~125℃


 卓越的ESD性能：HBM 6KV


 符合RoHS标准

### 2 典型应用


–
3D 磁场开关量检测


–电表/水表/燃气表防窃检测


–智能门窗检测


–电动车库门检测

### **3 概述**


KTH4603系列是一款具有X、Y、Z三维全极检测的低功耗


霍尔效应开关传感器。该芯片可以提供多种开关工作频


率和封装形式以适配各种应用。


当施加的S极或N极磁感应强度超过工作点B OP 时，芯片输


出低电平，且保持低电平。直到S极或N极磁感应强度低


于释放点B RP 时，芯片输出高电平。芯片内置X,Y,Z三个


超灵敏低失调的霍尔盘、多路模拟开关、差分放大器、


施密特触发器和NMOS开漏输出电路，采用了先进SPIN及


数字滤波技术、优化时钟控制技术从而保证芯片稳定的


工作点和开关频率。


KTH4603系列可以在2.5V至5.5V的供电电压范围内工作，


并采用标准的SOT-23-3L、SOT-23-6L封装。


昆泰芯微电子科技有限公司
**1**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

SOT-23-3L


SOT-23-6L


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

SOT-23-3L


KTH4603XX-ST3


SOT-23-6L

|引脚名称|引脚序号|功能描述|
|---|---|---|
|~~VDD~~<br>|~~1~~<br>|供电输入端|
|~~OUT~~<br>|~~2~~<br>|输出端|
|~~GND~~|~~3~~|地|



KTH4603XX-ST6

|引脚名称|引脚序号|功能描述|
|---|---|---|
|~~VDD~~<br>|~~1~~<br>|供电输入端|
|~~TEST~~<br>|~~2~~<br>|接地<br>|
|~~OUTX~~<br>|~~3~~<br>|~~X~~ 轴输出<br>|
|~~OUTY~~<br>|~~4~~<br>|~~Y~~ 轴输出|
|~~GND~~<br>|~~5~~<br>|地|
|~~OUTZ~~|~~6~~|Z 轴输出|



昆泰芯微电子科技有限公司
**2**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

### **6 开关输出特性**

对于KTH4603XX-ST3的单输出选项，当一个磁场垂直于其中任何一个霍尔传感器，无论是X、Y还是Z方向，


当施加的磁感应强度大于B OPS (或小于B OPN )时，芯片输出为低(开关闭合)。KTH4603XX-ST6具有三个单独的输出(X,


Y或Z)，当有磁场施加于霍尔芯片时，无论X轴或Y轴或Z轴磁场只要对应方向的磁场强度超过了工作点B OPS (或小


于B OPN )时对应的输出引脚则输出低电平(开关闭合);当对应的磁感应强度降低到B RPS 点以下(或增加到B RPN 点以上)


对应的输出引脚则输出高电平(开关打开)。操作点和释放点的磁感应强度的差值是磁滞(B HY ),这种内置的磁滞


使得芯片可以稳定输出，不受机械振动和磁噪声所干扰。芯片上电工作后当磁感应强度在滞回区即B OP 和B RP 之间


时输出为不确定状态，可确认的输出状态是由第一个超出B OP 或B RP 的磁场来决定的。


昆泰芯微电子科技有限公司
**3**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

### 8 绝对最大额定值

TA=25℃(除特别说明外)


列出的所有电压均以GND 为参考。

|项目|参数说明|Min|Max|单位|
|---|---|---|---|---|
|VDD|供电电压|-0.3|6|V|
|IOUTPUT|输出驱动电流||30|mA|
|B|磁感应强度||无上限|GS|
|TSTG|存储温度范围|-50|150|℃|
|TJ|结点最高耐温||150|℃|
|ESD HBM|人体模型ESD 能力|-6000|6000|V|



注： 超过绝对最大额定值可能造成永久性损坏。长时间工作于绝对最大额定条件下可能会影响芯片的可靠性。


昆泰芯微电子科技有限公司
**4**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

TA=25℃(除特别说明外)

|项目|参数说明|工作条件|数值|单位|
|---|---|---|---|---|
|VDD|供电电压范围|芯片工作|2.5～5.5|V|
|TA|工作温度范围|芯片工作|-40～125|oC|




### **10 电参数**


TA=25℃,VDD=3.3V (除特别说明外)














|参数符号|参数说明|测试条件|最小值|典型值|最大值|单位|
|---|---|---|---|---|---|---|
|VDD|供电电压||2.5|3.3|5.5|V|
|IDD|唤醒功耗|VDD=2.5V,TA=25℃|-|2.7|-|mA|
|IDD|休眠功耗|VDD=2.5V,TA=25℃|-|2.5|-|uA|
|IDD|平均功耗<br>（KTH4603AA)|VDD=2.5V,TA=25℃|-|4.5|-|uA|
|IDD|平均功耗<br>（KTH4603AA)|VDD=5.0V,TA=25℃|-|6|-|uA|
|IDD|平均功耗<br>(KTH4603AB)|VDD=2.5V,TA=25℃|-|7.1|-|uA|
|IDD|平均功耗<br>(KTH4603AB)|VDD=5.0V,TA=25℃|-|9|-|uA|
|IOUTOFF|输出漏电流||B|<|BRP||-|-|10|uA|
|VOUT|输出电压|IOUT=2mA,B>BOP|-|20|-|mV|
|TAWAKE|唤醒时间||-|405|-|us|
|Tperiod|周期|KTH4603AA系列|-|408|-|ms|
|Tperiod|周期|KTH4603AB系列|-|205|-|ms|



注：为了保持芯片的低平均功率，内部采样电路定时处于Awake/Sleep 状态，传感器每轴通电135us 之后进入


低功耗睡眠模式。这个Awake 和Sleep 周期在每个周期中发生三次，这样X、Y、Z 轴都在相应周期中进行采样，


短暂的“Awake”时间内芯片对磁场进行采样和保持并输出对应的结果，并在每个周期结束时进行数据锁定。


每个Sleep 睡眠周期期间的输出状态将被保持当前判断状态，同时输出为高/低电平的状态不影响芯片的工作


昆泰芯微电子科技有限公司
**5**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

### **11 磁参数**

TA=25℃,VDD=3.3V (除特别说明外)















|参数符号|参数说明|测试条件|最小值|典型值|最大值|单位|
|---|---|---|---|---|---|---|
|**BOPS**|工作点|南极向左，底部或有打印标记的面侧（参见图1)|-|25|40|GS|
|**BOPN**|**BOPN**|北极向左，底部或有打印标记的面侧（参见图1)|-40|-25|-|GS|
|**BRPS**|释放点|南极向左，底部或有打印标记的面侧（参见图1)|5|15|-|GS|
|**BRPN**|**BRPN**|北极向左，底部或有打印标记的面侧（参见图1)|-|-15|-5|GS|
|**BHY**|磁滞|BHY=(|BOP - BRP|)|-|10|-|GS|


图 1


磁体取向的三维示意图


昆泰芯微电子科技有限公司
**6**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

平均功耗VS 供电电压@TA=25℃ 平均功耗VS 工作温度@VDD=3.3V


低输出电压VS 供电电压@TA=25℃ 低输出电压VS 工作温度@VDD=3.3V


IOUT=20mA IOUT=20mA


工作周期VS 供电电压@TA=25℃ 工作周期VS 工作温度@VDD=3.3V


昆泰芯微电子科技有限公司
**7**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

X 轴磁场阈值VS 供电电压@TA=25℃ X 轴磁场阈值VS 工作温度@VDD=3.3V


Y 轴磁场阈值VS 供电电压@TA=25℃ Y 轴磁场阈值VS 工作温度@VDD=3.3V


Z 轴磁场阈值VS 供电电压@TA=25℃ Z 轴磁场阈值VS 工作温度@VDD=3.3V


昆泰芯微电子科技有限公司
**8**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

X 轴磁场磁滞VS 供电电压@TA=25℃ X 轴磁场磁滞VS 工作温度@VDD=3.3V


Y 轴磁场磁滞VS 供电电压@TA=25℃ Y 轴磁场磁滞VS 工作温度@VDD=3.3V


Z 轴磁场磁滞VS 供电电压@TA=25℃ Z 轴磁场磁滞VS 工作温度@VDD=3.3V


昆泰芯微电子科技有限公司
**9**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关**

|型号|封装形式|引脚数|磁场阈值（Bop）|开关频率|温度|
|---|---|---|---|---|---|
|KTH4603AA-ST3|SOT-23-3L|3|25Gauss|2.5Hz|-40℃~125℃|
|KTH4603AB-ST3|SOT-23-3L|3|25Gauss|5Hz|-40℃~125℃|
|KTH4603AA-ST6|SOT-23-6L|6|25Gauss|2.5Hz|-40℃~125℃|
|KTH4603AB-ST6|SOT-23-6L|6|25Gauss|5Hz|-40℃~125℃|


### **14 典型应用**

KTH4603XX 在2.5V 到5.5 V 的输入电压范围内工作,为了滤除芯片电源端的噪声，KTH4603XX 也需要增加所有


芯片都必须增加的元件即电源和地之间的滤波电容，该电容大小推荐为1μF 且此电容尽量接近VDD 引脚。通


常，在KTH4603XX 器件下方使用PCB 铜层对磁感应强度没有影响，也不会干扰器件性能。这是因为铜不是铁磁


材料。但是，如果附近的系统组件含有铁或镍，它们可能会以不可预测的方式改变磁感应强度。


KTH4603XX-ST3 典型应用


KTH4603XX-ST6 典型应用


昆泰芯微电子科技有限公司
**10**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关** SOT-23-3L 封装信息



|Symbol|Dimensions in Millimeters|Col3|Col4|
|---|---|---|---|
|**Symbol**|**Min.**|**Typ.**|**Max.**|
|A|-|-|1.25|
|A1|0.00|-|0.1|
|A2|1.00|1.10|1.15|
|b|0.30|-|0.50|
|c|0.10|-|0.20|
|D|2.82|2.95|3.02|
|E|2.65|2.80|2.95|
|E1|1.50|1.65|1.70|
|e|0.85|0.95|1.05|
|e1|1.80|1.90|2.00|
|L|0.30|0.45|0.60|
|θ|0︒|-|8︒|


昆泰芯微电子科技有限公司
**11**


# **KTH4603 系列**

### **微功耗超灵敏的3D 霍尔开关** SOT-23-6L 封装信息

|Symbol|Dimensions In Millimeters|Col3|Dimensions In Inches|Col5|
|---|---|---|---|---|
|**Symbol**|**Min**|**Max**|**Min**|**Max**|
|**A**|**1.050**|**1.280**|**0.041**|**0.050**|
|**A1**|**0.000**|**0.130**|**0.000**|**0.005**|
|**A2**|**1.050**<br>|**1.150**<br>|**0.041**<br>|**0.045**<br>|
|**b**|~~**0.300**~~|~~**0.500**~~|~~**0.012**~~|~~**0.020**~~|
|**c**|**0.100**|**0.200**|**0.004**|**0.008**|
|**D**|**2.820**<br>|**3.020**<br>|**0.111**<br>|**0.119**<br>|
|**E1**|~~**1.500**~~|~~**1.720**~~|~~**0.059**~~|~~**0.068**~~|
|**E**|**2.650**|**3.000**|**0.104**|**0.118**|
|**e**|**0.950（BSC）**<br><br>|**0.950（BSC）**<br><br>|**0.037（BSC）**<br><br>|**0.037（BSC）**<br><br>|
|**e1**|~~**1.800**~~|~~**2.000**~~|~~**0.071**~~|~~**0.079**~~|
|**L**|**0.300**|**0.600**|**0.012**|**0.024**|
|**L1**|**0.600REF**<br><br>|**0.600REF**<br><br>|**0.024REF**<br><br>|**0.024REF**<br><br>|
|θ|~~**0°**~~|~~**8°**~~|~~**0°**~~|~~**8°**~~|



昆泰芯微电子科技有限公司
**12**




</details>

---

## 相关资源

### PDF文档
- [📋 KTH4603 Datasheet_EN.pdf](/pdfs/KTH4603 Datasheet_EN.pdf)
- [📋 KTH4603XX产品手册V1.0.pdf](/pdfs/KTH4603XX产品手册V1.0.pdf)

### 其他资源
- [产品选型指南](../technical/)
- [应用案例](../technical/)
- [技术支持](../technical/)

---

## 技术支持

如需技术支持、样品申请或定制化服务，请联系我们：

- 📧 邮箱: support@ktsense.com
- 📞 技术热线: 400-xxx-xxxx
- 🌐 在线支持: [技术论坛](../technical/)

---

*最后更新: 2024年*
*版本: Enhanced v1.0*
*包含完整PDF内容和技术图片*


## 🔗 相关产品推荐

### 霍尔开关

- [KTH1631 增强版](./KTH1631.md) - 同系列产品
- [KTH2502 增强版](./KTH2502.md) - 同系列产品
- [KTH1701 增强版](./KTH1701.md) - 同系列产品
### 3D霍尔传感器

- [KTH31xx 增强版](./KTH31xx.md) - 推荐3D霍尔传感器
### 磁编码器

- [KTH7801 增强版](./KTH7801.md) - 推荐磁编码器
### 其他传感器

- [KTAX333 增强版](./KTAX333.md) - 推荐其他传感器

---
