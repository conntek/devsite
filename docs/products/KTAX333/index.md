# KTAx333系列 - 零漂移微功耗CMOS运算放大器

## 📋 PDF资料下载

- **[📄 KTAx333_DATASHEET_en.pdf](/pdfs/KTAx333_DATASHEET_en.pdf)** - 完整技术规格书（英文版）

---

## 🧭 页面导航

- 🔙 [返回产品摘要页面](../other-sensors/KTAX333.md)
- 📂 [返回其他传感器分类](../other-sensors/)
- 🏠 [返回主页](../index.md)
- 📚 [所有增强版技术参考](./index.md)

---

## 🔍 产品概述

KTAx333系列是一款高性能零漂移微功耗CMOS运算放大器，采用先进的斩波稳定技术和自动校零技术。该系列产品具有极低的输入失调电压、超低功耗、轨到轨输入输出等特点，特别适用于精密测量、传感器信号调理、电池供电设备等应用。

### 核心特性
- **零漂移技术**：采用斩波稳定和自动校零技术
- **微功耗设计**：超低静态电流消耗
- **轨到轨输入输出**：充分利用电源电压范围
- **高精度**：极低输入失调电压和温漂
- **宽工作电压**：单电源或双电源供电
- **高输入阻抗**：CMOS输入级设计
- **低噪声**：优异的噪声性能

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

## 📄 KTAx333_DATASHEET_en.pdf

<details>
<summary>点击展开 KTAx333_DATASHEET_en.pdf 完整内容</summary>

# KTAx333 Series

## Zero-Drift, Micro-Power CMOS Operational Amplifiers

### Technical Support sales.global@conntek.com.cn

2024- 8- 9


Disclaimer


The information in this document is provided by Quanzhou KTsense Microelectronics Co., Ltd. (泉州昆泰芯微电子科技有限公司)
(hereafter referred to as ”KTsense Micro”) on an ”as is” basis for informational purposes only. KTsense Micro does not guarantee the
accuracy of the information contained herein or the outcomes of its implementation. KTsense Micro assumes no liability for any
errors or inaccuracies that may be present in this document. Users assume full responsibility for the application of the practices
outlined in this document.


KTsense Micro owns the registered trademark CONNTEK, under which the CONNTEK brand sensors are marketed.


This document comes without any warranties, express or implied, including but not limited to warranties of merchantability, satisfactory quality, non-infringement, and fitness for a particular purpose. KTsense Micro, along with its employees, agents, and affiliates, is not liable for any losses arising from the use or reliance on this document.


This document is subject to change without prior notice and should not be construed as a commitment by KTsense Micro. Users
should ensure they have the latest version of the relevant information before placing orders or integrating the product into their
systems.


Users must evaluate the suitability of the product described in this document for their specific applications, including the required
level of reliability and fitness for purpose.


This document and the described product may be subject to export control regulations. Export may require prior authorization from
the competent authorities. The product is not intended, authorized, or warranted for use in applications requiring extended temperature ranges or unusual environmental conditions. High reliability applications, such as medical life-support or aviation systems, are
specifically excluded.


The product may not be used for the development, production, maintenance, or storage of:


1. Chemical, biological, or nuclear weapons, including missile systems for such weapons.
2. Civil firearms, including spare parts or ammunition.
3. Defense-related products or materials for military or law enforcement use.
4. Applications that could cause serious harm to persons or property and that can be used as a means of violence in armed
conflicts or similar situations.


No licenses or rights to any intellectual property of KTsense Micro or third parties are granted.


If this document is marked as “confidential”or similar, or if the content is reasonably understood to be confidential, the recipient
must not disclose any part of the document to third parties without the express written consent of KTsense Micro. The recipient
must take all necessary measures to maintain the confidentiality of the document, using at least the same degree of care as they
use to protect their own confidential information, but no less than a reasonable degree of care. The recipient may only disclose
the document to employees on a need-to-know basis, provided they are bound by confidentiality terms similar to those in this disclaimer. The document may only be used for the purpose for which it was received and may not be used for commercial purposes
or to the detriment of KTsense Micro or its customers. These confidentiality obligations will last indefinitely but in any case, for no
less than 10 years from the receipt of the document.


This disclaimer is governed by the laws of China, and any disputes arising from it will be subject to the exclusive jurisdiction of the
courts in Shenzhen, China.


The invalidity of any provision in this disclaimer does not affect the validity of the remaining provisions. Previous versions of this
document are repealed.


Copyright


This document and its contents are protected by copyright law. No part of this document may be reproduced or distributed in any
form or manner without the prior written consent of KTsense Micro.


Contact Information


[For the latest version of this document, go to our website at https://en.conntek.com.cn/.](https://en.conntek.com.cn/)


For additional information, please contact our Direct Sales team and get help for your specific needs:


KTAx333 Series

|Region|Contact Information|
|---|---|
|Overseas|Email: sales.global@conntek.com.cn|
|China|Email: sales@conntek.com.cn|



3 of 19


## Table of Contents

**1 Key Features** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **5**


**2 Typical Applications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **5**


**3 Overview** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **5**


**4 Pin Configuration and Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **6**


**4.1** KTA333 Pin Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

**4.2** KTA2333 Pin Functions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

**4.3** KTAx333 Series Part Name Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


**5 Specifications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **7**


**5.1** Absolute Maximum Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
**5.2** ESD Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
**5.3** Recommended Operating Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8


**6 Electrical Characteristics** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **8**


**6.1** Input Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
**6.2** Output Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
**6.3** Power Supply . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
**6.4** Frequency Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

**6.5** Noise Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

**6.6** Temperature Characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**7 Typical Characteristics** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **9**


**8 Application Guide** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **10**


**8.1** Operating Voltage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
**8.2** Rail-to-Rail Input/Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
**8.3** Input Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

**8.4** Internal Offset Correction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

**8.5** Residual Ripple. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


**9 Typical Applications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **12**


**9.1** Temperature Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

**9.2** Thermistor Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

**9.3** Low-Side Current Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
**9.4** High-Side Current Monitoring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
**9.5** Instrumentation Amplifier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**10 Ordering Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **14**


**11 Package Dimensions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **15**


**11.1** SOT23-5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15


**11.2** SC70-5 (SOT353) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

**11.3** SOP-8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

**11.4** MSOP-8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

**11.5** DFN-2 _×_ 2-8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


KTAx333 Series

## 1 Key Features

### • [Low offset voltage:] – [2] [ µV] [ (typical)] – [10] [ µV] [ (maximum)] • [Zero-drift:][ 0] [.] [05] [ µV] [ /] [◦] [C (maximum)] • [Micro-power:] – [17] [ µA] [ (single channel)] – [30] [ µA] [ (dual channel)] • [Rail-to-rail input/output] • [Wide supply voltage range:][ 1] [.] [8] [ V][ −] [5] [.] [5] [ V] • [Low][ 0] [.] [1][ Hz] [ −] [10][ Hz noise:][ 1] [.] [1] [ µV] • [Single-supply operation]

## 2 Typical Applications

### • [Sensors] • [Temperature measurement] • [Electronic scales] • [Bridge circuit readout] • [Medical instruments]

## 3 Overview


The KTAx333 is a single-supply, low-power CMOS operational amplifier
capable of rail-to-rail input and output. It employs self-calibration technology to achieve an extremely low offset voltage (2 _µV_, typical) with
nearly zero drift over temperature and time. The amplifier offers high input impedance (common-mode range exceeding the supply rail voltage
by 100 _mV_ ) and can operate with a single supply from 1 _._ 8 _V_ ( _±_ 0 _._ 9 _V_ ) up
to 5 _._ 5 _V_ ( _±_ 2 _._ 75 _V_ ), or with dual supplies.


The KTAx333 series delivers excellent common-mode rejection ratio
(CMRR) performance without the crossover distortion associated with
traditional complementary input stages. This design enables outstanding
performance when driving analog-to-digital converters (ADCs) without
sacrificing differential linearity.


The KTA333 (single-channel) is available in 5-pin SOT-23-5, SC70-5,
and SOP-8 packages. The KTA2333 (dual-channel version) is available
in SOP-8, MSOP-8, and DFN-2 _×_ 2-8 packages.


5 of 19


KTAx333 Series

## 4 Pin Configuration and Functions


4.1 KTA333 Pin Functions


Figure 1: KTAx333 Package and Pin Functions

|Pin Name|Pin of SOP|Pin of SOT|Pin of SC70|I/O|Description|
|---|---|---|---|---|---|
|IN+<br>IN-<br>NC<br>OUT<br>V+<br>V-|3<br>2<br>1, 5, 8<br>6<br>7<br>4|3<br>4<br>—<br>1<br>5<br>2|1<br>3<br>—<br>4<br>5<br>2|I<br>I<br>—<br>O<br>—<br>—|Non-inverting input<br>Inverting input<br>No connection (can be left floating)<br>Output<br>Positive power supply<br>Negative power supply|



Table 1: KTA333 Pin Configuration


6 of 19


KTAx333 Series


4.2 KTA2333 Pin Functions

|Pin Name|Pin of DFN|Pin of SOP/MSOP|I/O|Description|
|---|---|---|---|---|
|INA+<br>INA-<br>INB+<br>INB-<br>OUTA<br>OUTB<br>V+<br>V-|3<br>2<br>5<br>6<br>1<br>7<br>8<br>4|3<br>2<br>5<br>6<br>1<br>7<br>8<br>4|I<br>I<br>I<br>I<br>O<br>O<br>—<br>—|Non-inverting input, channel A<br>Inverting input, channel A<br>Non-inverting input, channel B<br>Inverting input, channel B<br>Output, channel A<br>Output, channel B<br>Positive power supply<br>Negative power supply|



Table 2: KTA2333 Pin Configuration


4.3 KTAx333 Series Part Name Definition


Figure 2: KTAx333 Part Name Definition

## 5 Specifications


5.1 Absolute Maximum Ratings

|Parameter|Min|Max|
|---|---|---|
|Supply Voltage_ VCC_<br>Input Voltage_ VIN_<br>Junction Temperature_ TJ_<br>Storage Temperature_ TST G_|6_._5_ V_<br>_V −_-0.2V<br>_−_65 _◦_C|_V_ ++0.2V<br>150 _◦_C<br>150 _◦_C|



Table 3: Absolute Maximum Ratings


Note: Exceeding the absolute maximum ratings may cause permanent
damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indi

7 of 19


KTAx333 Series


cated in the operational sections of this specification is not implied. Prolonged operation at the maximum absolute rating conditions may affect
device reliability.


5.2 ESD Ratings

|Parameter|Value|
|---|---|
|Human Body Model (HBM)|7 kV|



Table 4: ESD Ratings


5.3 Recommended Operating Conditions

|Parameter|Min|Max|
|---|---|---|
|Supply Voltage_ VCC_<br>Operating Temperature Range_ TA_|1_._8_ V_<br>_−_40 _◦_C|5_._5_ V_<br>125 _◦_C|



Table 5: Recommended Operating Conditions

## 6 Electrical Characteristics


Conditions: @ _T_ _A_ =+25 _[◦]_ C, _V_ _CM_ =Vs/2, VOUT=Vs/2, unless otherwise noted.


6.1 Input Characteristics










|Parameter Name|Description|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|_VOS_<br>_dVOS_/_dT_<br>_IB_<br>_IOS_<br>_VCM_<br>_CMRR_<br>_AOL_|Offset Voltage<br>Offset Voltage<br>Drift<br>Input Bias Cur-<br>rent<br>Input Offset<br>Current<br>Common Mode<br>Voltage Range<br>Common Mode<br>Rejection Ratio<br>Open-Loop<br>Voltage Gain|_VS_ = 5_ V_<br>_TA_ =_ −_40_◦_C to 125_◦_C<br>(_V −_)_ −_0_._1_ V < VCM <_<br>(_V_ +) + 0_._1_ V_,_ TA_ =<br>_−_40_◦_C to 125_◦_C<br>(_V −_) + 100_mV < VO <_<br>(_V_ +)_ −_100_mV_,_ RL_ =<br>10_ k_Ω,_ TA_ =_ −_40_◦_C to<br>125_◦_C|(_V −_)_ −_0_._1|2<br>0.02<br>_±_100<br>_±_120<br>120<br>120|10<br>0.05<br>(_V_ +) + 0_._1|_µV_<br>_µV_ /_◦_C<br>pA<br>pA<br>_V_<br>dB<br>dB|



Table 6: Input Characteristics



8 of 19


KTAx333 Series


6.2 Output Characteristics

|Parameter Name|Description|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Output Swing relative to Power Rails|Output Swing relative to Power Rails|_RL_ = 10 kΩ||30|70|mV|
|_ISC_|Short-Circuit Current|||_±_17||mA|



Table 7: Output Characteristics


6.3 Power Supply







|Parameter Name|Description|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|_VS_<br>_IQ_<br>_IQ_<br>_PSRR_|Supply Voltage Range<br>Quiescent Current (Single)<br>Quiescent Current (Dual)<br>Power Supply Rejection Ratio|_IO_ = 0_ A_,_ TA_ =_ −_40_◦C_ to<br>125_◦C_, signle amplier<br>_IO_ = 0_ A_,_ TA_ =_ −_40_◦C_ to<br>125_◦C_, dual ampliers<br>_VS_ = 1_._8_ V_ to 5_._5_ V_,<br>_TA_ =_ −_40_◦C_ to 125_◦C_|1.8|17<br>30<br>1|5.5<br>5|_V_<br>_µA_<br>_µA_<br>_µV_ /_V_|
|Turn-on Time|Turn-on Time|_VS_ = 5_V_||200||_µs_|


Table 8: Power Supply Characteristics


6.4 Frequency Characteristics

|Parameter Name|Description|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|_GBW_<br>_SR_|Gain Bandwidth Product<br>Slew Rate|_CL_ = 100_ pF_<br>_G_ = 1||350<br>0.16||kHz<br>_V_ /_µs_|



Table 9: Frequency Characteristics


6.5 Noise Characteristics

|Parameter Name|Description|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Input Noise|Input Noise|_f_ = 0_._1 Hz to 10 Hz||1.1||_µVP P_|



Table 10: Noise Characteristics


6.6 Temperature Characteristics

|Parameter Name|Description|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|_TA_|Operating Temperature Range||-40||125|_◦_C|



Table 11: Temperature Characteristics

## 7 Typical Characteristics


(@ _T_ _A_ = +25 _[◦]_ C, _V_ _S_ = 5V, _C_ _L_ = 0pF, unless otherwise noted.)


9 of 19


KTAx333 Series


Figure 3: Offset Voltage Distribution Figure 4: 0.1Hz to 10Hz Noise


Figure 5: Large Signal Step Response Figure 6: Small Signal Step Response


Figure 7: Negative Overvoltage Recovery Figure 8: Positive Overvoltage Recovery



Figure 9: Quiescent Current vs.
Temperature

## 8 Application Guide



Figure 10: Output Voltage Swing vs.
Output Current



The KTAx333 series operational amplifiers feature unity-gain stability
and are suitable for a wide range of general-purpose applications. They
offer very low offset voltage with minimal drift over time and temperature variations.


10 of 19


KTAx333 Series


8.1 Operating Voltage


The KTAx333 series operational amplifiers can operate with a single supply voltage ranging from 1 _._ 8 _V_ to 5 _._ 5 _V_, or a dual supply ranging from
_±_ 0 _._ 9 _V_ to _±_ 2 _._ 75 _V_ . Operating beyond the absolute maximum voltage
of 6 _._ 5 _V_ can permanently damage the device. To achieve better performance, a 0.1 _µ_ F bypass capacitor should be placed near the power supply pins.


8.2 Rail-to-Rail Input/Output


The KTAx333 series features rail-to-rail input and output capabilities,
providing a wide input common-mode voltage range that exceeds the
supply voltage by 100 _mV_ . The output swing can achieve within 100 _mV_
of the supply rails under a 10 _k_ Ω load.


8.3 Input Protection


The KTAx333 series includes internal ESD protection diodes connected
between the input pins and the supply rails, as shown in Figure 11. These
diodes conduct when the input voltage exceeds either supply rail by 300
mV, providing over-voltage protection. However, if the current flowing through the diodes exceeds 10 mA, the device may be permanently
damaged. To prevent this, an input resistor can be used, as shown in
Figure 12.


Figure 11: Input ESD Protection Structure


11 of 19


KTAx333 Series


Figure 12: Input Current Protection


8.4 Internal Offset Correction


The KTAx333 series operational amplifiers use a chopper stabilization
technique combined with a continuous-time signal chain. This amplifier
performs offset correction every 10 _µs_, and after power-on, it requires
approximately 200 _µs_ to reach the specified offset accuracy. The use of
chopper stabilization also eliminates 1/f noise.


8.5 Residual Ripple


The KTAx333 series operational amplifiers use chopper-stabilization
technology to eliminate offset voltage, while a notch filter is employed
to suppress ripple caused by the chopper modulation. Although the ripple voltage is reduced, significant residual noise energy remains at the
chopper frequency and its harmonics. To further attenuate noise at the
chopper frequency, it is recommended to add a post-filter at the output
of the operational amplifier.

## 9 Typical Applications


9.1 Temperature Measurement


Figure 13: Temperature Measurement Application


12 of 19


KTAx333 Series


9.2 Thermistor Measurement


Figure 14: Thermistor Measurement Application


9.3 Low-Side Current Monitoring


Figure 15: Low-Side Current Monitoring


9.4 High-Side Current Monitoring


Figure 16: High-Side Current Monitoring


13 of 19


KTAx333 Series


9.5 Instrumentation Amplifier


Figure 17: Instrumentation Amplifier Application

## 10 Ordering Information

|Model|Package Type|Pin Count|Standard Package Quantity|Temperature Range|
|---|---|---|---|---|
|KTA333-ST5<br>KTA2333-MP8<br>KTA333-SF5*<br>KTA333-SC5*<br>KTA333-SP8*<br>KTA2333-DZ8*<br>KTA2333-SP8|SOT23-5<br>MSOP-8<br>SOT353-5<br>SC70-5<br>SOP-8<br>DFN-2_×_2-8<br>SOP-8|5<br>8<br>5<br>5<br>8<br>8<br>8|3000<br>4000<br>—<br>—<br>—<br>—<br>4000|-40_◦_Cto125_◦_C<br>-40_◦_Cto125_◦_C<br>-40_◦_Cto125_◦_C<br>-40_◦_Cto125_◦_C<br>-40_◦_Cto125_◦_C<br>-40_◦_Cto125_◦_C<br>-40_◦_Cto125_◦_C|



Table 12: Ordering Information for KTAx333 Series


Note:Models marked with *are currently available only as sample quantities and not for mass production.


14 of 19


KTAx333 Series

## 11 Package Dimensions


11.1 SOT23-5

|Symbol|Dimensions in Millimeters|Col3|Dimensions in Inches|Col5|
|---|---|---|---|---|
|Symbol|Min|Max|Min|Max|
|A<br>A1<br>A2<br>b<br>c<br>D<br>E<br>E1|1.050<br>0.000<br>1.050<br>0.300<br>0.100<br>2.820<br>2.650<br>1.500|1.250<br>0.100<br>1.150<br>0.500<br>0.200<br>3.020<br>2.950<br>1.700|0.041<br>0.000<br>0.041<br>0.012<br>0.004<br>0.111<br>0.104<br>0.059|0.049<br>0.004<br>0.045<br>0.020<br>0.008<br>0.119<br>0.116<br>0.067|
|e|0.950(BSC)|0.950(BSC)|0.037(BSC)|0.037(BSC)|
|e1<br>L<br>_θ_|1.800<br>0.300<br>0_◦_|2.000<br>0.600<br>8_◦_|0.071<br>0.012<br>0_◦_|0.079<br>0.024<br>8_◦_|



Table 13: SOT23-5 Package Dimensions


15 of 19


KTAx333 Series


11.2 SC70-5 (SOT353)

|Symbol|Dimensions in Millimeters|Col3|Dimensions in Inches|Col5|
|---|---|---|---|---|
|Symbol|Min|Max|Min|Max|
|A<br>A1<br>A2<br>b<br>c<br>D<br>E<br>E1|0.900<br>0.000<br>0.900<br>0.150<br>0.110<br>2.000<br>2.150<br>1.150|1.100<br>0.100<br>1.000<br>0.350<br>0.175<br>2.200<br>2.450<br>1.350|0.035<br>0.000<br>0.035<br>0.006<br>0.004<br>0.079<br>0.085<br>0.045|0.043<br>0.004<br>0.039<br>0.014<br>0.007<br>0.087<br>0.096<br>0.053|
|e|0.650(TYP)|0.650(TYP)|0.026(TYP)|0.026(TYP)|
|e1<br>L<br>L1|1.200<br>1.400<br>0.300<br>0.600<br>0.525(REF)|1.200<br>1.400<br>0.300<br>0.600<br>0.525(REF)|0.047<br>0.055<br>0.012<br>0.024<br>0.021(REF)|0.047<br>0.055<br>0.012<br>0.024<br>0.021(REF)|
|_θ_|0_◦_|8_◦_|0_◦_|8_◦_|



Table 14: SC70-5 Package Dimensions


16 of 19


KTAx333 Series


11.3 SOP-8

|Symbol|Dimensions in Millimeters|Col3|Dimensions in Inches|Col5|
|---|---|---|---|---|
|Symbol|Min|Max|Min|Max|
|A<br>A1<br>A2<br>b<br>c<br>D<br>E<br>E1|1.350<br>0.100<br>1.350<br>0.330<br>0.170<br>4.700<br>5.800<br>3.800|1.750<br>0.250<br>1.550<br>0.510<br>0.250<br>5.100<br>6.200<br>4.000|0.053<br>0.004<br>0.053<br>0.013<br>0.006<br>0.185<br>0.228<br>0.150|0.069<br>0.010<br>0.061<br>0.020<br>0.010<br>0.200<br>0.244<br>0.157|
|e|1.270(TYP)|1.270(TYP)|0.050(TYP)|0.050(TYP)|
|L|0.400|0.800|0.016|0.031|
|_θ_|0_◦_|8_◦_|0_◦_|8_◦_|



Table 15: SOP-8 Package Dimensions


17 of 19


KTAx333 Series


11.4 MSOP-8

|Symbol|Dimensions in Millimeters|Col3|Dimensions in Inches|Col5|
|---|---|---|---|---|
|Symbol|Min|Max|Min|Max|
|A<br>A1<br>A2<br>b<br>c<br>D<br>E<br>E1|0.820<br>0.020<br>0.750<br>0.250<br>0.090<br>2.900<br>4.750<br>2.900|1.100<br>0.150<br>0.950<br>0.380<br>0.230<br>3.100<br>5.050<br>3.100|0.032<br>0.001<br>0.030<br>0.010<br>0.004<br>0.114<br>0.187<br>0.114|0.043<br>0.006<br>0.037<br>0.015<br>0.009<br>0.122<br>0.199<br>0.122|
|e|0.650(TYP)|0.650(TYP)|0.026(TYP)|0.026(TYP)|
|L|0.400|0.800|0.016|0.031|
|_θ_|0_◦_|6_◦_|0_◦_|6_◦_|



Table 16: MSOP-8 Package Dimensions


18 of 19


KTAx333 Series


11.5 DFN-2 _×_ 2-8

|Symbol|Dimensions in Millimeters|Col3|Dimensions in Inches|Col5|
|---|---|---|---|---|
|Symbol|Min|Max|Min|Max|
|A<br>A1<br>A3<br>D<br>E<br>D1<br>E1<br>K|0.700<br>0.800<br>0.000<br>0.050<br>0.203(REF)<br>1.900<br>2.100<br>1.900<br>2.100<br>0.500<br>0.700<br>1.100<br>1.300<br>0.350(REF)|0.700<br>0.800<br>0.000<br>0.050<br>0.203(REF)<br>1.900<br>2.100<br>1.900<br>2.100<br>0.500<br>0.700<br>1.100<br>1.300<br>0.350(REF)|0.028<br>0.031<br>0.000<br>0.002<br>0.008(REF)<br>0.075<br>0.083<br>0.075<br>0.083<br>0.020<br>0.028<br>0.043<br>0.051<br>0.014(REF)|0.028<br>0.031<br>0.000<br>0.002<br>0.008(REF)<br>0.075<br>0.083<br>0.075<br>0.083<br>0.020<br>0.028<br>0.043<br>0.051<br>0.014(REF)|
|b<br>e|0.200<br>0.300<br>0.500(BSC)|0.200<br>0.300<br>0.500(BSC)|0.008<br>0.012<br>0.020(BSC)|0.008<br>0.012<br>0.020(BSC)|
|L|0.274|0.426|0.011|0.017|



Table 17: DFN-2 _×_ 2-8 Package Dimensions


19 of 19




</details>

---

## 📄 KTAx333产品手册.pdf

<details>
<summary>点击展开 KTAx333产品手册.pdf 完整内容</summary>

   2μV(典型值)


   10μV(最大值)


 零漂移：0.05μV/℃(最大值)


 微功耗


   17μA(单通道)


   - 30μA(双通道)


 轨到轨输入/输出


 宽电源电压范围：1.8V-5.5V


 低0.1Hz-10Hz噪声：1.1μV


 单电源供电


**2** 典型应用

 传感器


 温度检测


 电子称


 桥式电路读出


 医疗仪表


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

**3** 概述

KTAx333是一款单电源供电，微功耗，可以实现轨到


轨输入/输出的CMOS运算放大器。其使用自校准技术


以提供极低的失调电压（2μV，典型值），同时随温度


和时间的漂移接近为零。放大器可以提供高输入阻抗


（共模范围超过电源轨电压100mV），可以使用1.8V


（±0.9V）和高达5.5V（±2.75V）的单电源或者双


电源。


KTAx333系列提供出色的CMRR性能，而不存在与传


统互补输入级关联的交叉。该设计可在驱动模数转换


器（ADC）的过程中实现优异的性能，而不会降低微


分线性。


KTA333（单通道）可提供5引脚SOT-23-5、SC70-5


以及SOP-8的封装。而KTA2333（双通道版本）可提


供SOP-8、MSOP-8以及DFN-2×2-8封装。



昆泰芯微电子科技有限公司 **1** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

昆泰芯微电子科技有限公司 **2** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

引脚功能： **KTA333**

|引脚|Col2|Col3|Col4|I/O|说明|
|---|---|---|---|---|---|
|名称|**SOP**|**SOT**|**SC70**|**SC70**|**SC70**|
|IN+|3|3|1|I|同相输入|
|IN-|2|4|3|I|反相输入|
|NC|1、5、8|—|—|—|无内部链（可以悬空）|
|OUT|6|1|4|O|输出|
|V+|7|5|5|—|正电源（最高）|
|V-|4|2|2|—|负电源（最低）|



引脚功能： **KTA2333**

|引脚|Col2|Col3|I/O|说明|
|---|---|---|---|---|
|名称|**DFN**|**SOP**、**MSOP-8**|**SOP**、**MSOP-8**|**SOP**、**MSOP-8**|
|INA+|3|3|I|同相输入，通道A|
|INA-|2|2|I|反相输入，通道A|
|INB+|5|5|I|同相输入，通道B|
|INB-|6|6|I|反相输入，通道B|
|OUTA|1|1|O|输出，通道A|
|OUTB|7|7|O|输出，通道B|
|V+|8|8|—|正电源（最高）|
|V-|4|4|—|负电源（最低）|



产品型号构成


KTAX333-XXX


封装简称：ST5：SOT23-5


SF5：SOT353-5


SC5：SC70-5


SP8：SOP-8


MP8：MSOP-8


DZ8：DFN2020-8


通道数：空白：单通道


2：双通道


昆泰芯微电子科技有限公司 **3** **Rev 1.0**


请参阅 [(1)]


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**



|Col1|最小值|最大值|单位|
|---|---|---|---|
|电源电压|6.5||V|
|模拟输入电压|V- - 0.2|V+ + 0.2|V|
|运行结温，TJ||150|℃|
|贮存温度，Tstg|-65|150|℃|


(1) 超出绝对最大额定值下所列值的应力可能会对器件造成永久性损坏，这些仅为在应力额定值下的工作情


况，对于额定值下器件的功能性操作以及超出建议的工作条件下的任何其它操作，在此并未说明。长时间运行


在最大额定条件下会影响器件的可靠性。


**5.2 ESD** 额定值

|ESD|值|单位|
|---|---|---|
|HBM|7K|V|



**5.3** 建议的工作条件

|Col1|最小值|最大值|单位|
|---|---|---|---|
|电源电压|1.8|5.5|V|
|额定温度范围|-40|125|℃|



昆泰芯微电子科技有限公司 **4** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

**6** 电参数 **(@TA=+25** ℃， **V** **CM** **=Vs/2** ， **VOUT=Vs/2** ，除特别说明外 **)**









|项目|参数说明|工作条件|最小值|典型值|最大值|单位|
|---|---|---|---|---|---|---|
|输入特性|输入特性|输入特性|输入特性|输入特性|输入特性|输入特性|
|VOS|失调电压|Vs=5V||2|10|μV|
|dVOS/dT|输入失调电压漂移|TA= –40°C 至125°C||0.02|0.05|μV/℃|
|IB|输入偏置电流|||±100||pA|
|IOS|输入失调电流|||±120||pA|
|VCM|输入共模电压范围||(V–) – 0.1||(V+) + 0.1|V|
|CMRR|共模抑制比|(V–) – 0.1V < VCM < (V+) + 0.1V，<br>TA = –40°C 至125°C||120||dB|
|AOL|开环电压增益|(V–) + 100mV < VO < (V+) – 100mV，<br>RL = 10kΩ，TA = –40°C 至125°C||120||dB|
|输出特性|输出特性|输出特性|输出特性|输出特性|输出特性|输出特性|
|相对于电源轨的输出摆幅|相对于电源轨的输出摆幅|RL=10K||30|70|mV|
|ISC|短路电流|||±17||mA|
|电源|电源|电源|电源|电源|电源|电源|
|VS|额定电压范围||1.8||5.5|V|
|IQ|静态功耗|IO=0A，TA= –40°C 至125°C（单运放）||17||μA|
|IQ|静态功耗|IO=0A，TA= –40°C 至125°C（双运放）||30||μA|
|PSRR|电源抑制比|VS=1.8V 至5.5V，TA= –40°C 至125°C||1|5|μV/V|
|开通时间|开通时间|VS=+5V||200||μs|
|频率特性|频率特性|频率特性|频率特性|频率特性|频率特性|频率特性|
|GBW|增益带宽积|CL=100pF||350||KHz|
|SR|压摆率|G=1||0.16||V/μs|
|噪声|噪声|噪声|噪声|噪声|噪声|噪声|
|输入噪声|输入噪声|F=0.1Hz 至10Hz||1.1||μVPP|
|温度|温度|温度|温度|温度|温度|温度|
|TA|额定温度范围||-40||125|℃|


昆泰芯微电子科技有限公司 **5** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

**7** 典型特性 **(@TA=+25** ℃， **Vs=5V** ， **C** **L** **=0pF** ，除特别说明外 **)**


图1.失调电压产生分布 图2.0.1Hz至10Hz噪声


图3.大信号阶跃响应 图4.小信号阶跃响应


图5.负过压恢复 图6.正过压恢复


昆泰芯微电子科技有限公司 **6** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

图7.静态电流与温度的关系 图8.输出电压摆幅与输出电流的关系


昆泰芯微电子科技有限公司 **7** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

KTAx333系列运算放大器具有单位增益稳定特性，且适用于各种通用应用。它可以提供非常低的失调电压并且随


时间推移和温度变化实现极低的温漂。


**8.1** 工作电压


KTAx333系列运算放大器可以使用 1.8V 到 5.5V 的单电源供电，也可以使用 ±0.9V 到 ±2.75V 的双电源供电。


高于 +6.5V（绝对最大值）的电源电压会对器件造成永久性损坏。为了获得更好的性能，在电源引脚附近应该


放置一个0.1μF的旁路电容。


**8.2** 轨到轨输入和输出


KTAx333系列运放具有轨到轨输入和轨到轨输出的特性。通过使用互补输入对结构可以获得很宽的输入共模电压


范围（超过电源轨100mV）。在10kΩ阻性负载条件下，输出电压摆幅可以达到小于电源轨100mV。


**8.3** 输入保护


KTAx333系列运算放大器输入端拥有两个内部ESD保护二极管，连接于电源轨和输入之间，如图9所示。当输入电


压高于任一电源轨300mV时，二极管正向导通泄放大电流以保护内部器件。通常，输入偏置电流约为100pA；但


是超过电源电压的输入电压可能导致过电流流入或流出输入引脚，如果电流超过10mA可能导致器件的永久损


坏。可通过输入电阻轻松实现此限制，如图10所示。


图9.输入ESD结构 图10.输入电流保护


**8.4** 内部偏移校正


KTAx333系列运算放大器使用斩波自校准技术与连续时间信号链结合使用，该放大器每10μs做一次失调校正。启


动后，放大器需要约200μs来实现额定Vos精度。斩波自校准技术的使用同时会消除闪烁噪声。


**8.5** 残余纹波


KTAx333系列运算放大器使用斩波自校准技术来消除运放的失调电压，同时使用陷波滤波器滤除由斩波调制引起


的纹波。尽管该纹波电压被抑制，但是斩波频率及其谐波分量上仍然存在比较大的残余噪声能量。为了更好地


滤除斩波频率处的噪声，推荐在运算放大器的输出端加一级后置滤波器。


昆泰芯微电子科技有限公司 **8** **Rev 1.0**


**9.1** 温度测量


图11显示了温度测量应用。


**9.2** 热敏电阻测量


图12显示了热敏电阻测量应用。


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

图11.温度测量


图12.热敏电阻测量



昆泰芯微电子科技有限公司 **9** **Rev 1.0**


图13显示了低侧电流监控应用。


**9.4** 高侧电流监控


图14显示了高侧电流监控应用。


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

图13.低侧电流监控


图14.高侧电流监控



昆泰芯微电子科技有限公司 **10** **Rev 1.0**


图15显示了仪表放大器应用。


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

图15.仪表放大器



昆泰芯微电子科技有限公司 **11** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**

|订货信息|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|型号|封装形式|引脚数|封装数量|温度|
|KTA333-ST5|SOT23-5|5|3000|-40℃~125℃|
|KTA2333-MP8|MSOP-8|8|4000|-40℃~125℃|
|KTA333-SF5*|SOT353-5|5|-|-40℃~125℃|
|KTA333-SC5*|SC70-5|5|-|-40℃~125℃|
|KTA333-SP8*|SOP-8|8|-|-40℃~125℃|
|KTA2333-DZ8*|DFN2020-8|8|-|-40℃~125℃|
|KTA2333-SP8|SOP-8|8|4000|-40℃~125℃|



*产品暂时只提供少量样品，不支持大规模供货。


昆泰芯微电子科技有限公司 **12** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**











|Symbol|Dimensions in<br>Millimeters|Col3|Dimensions in<br>Inches|Col5|
|---|---|---|---|---|
|**Symbol**|**Min**|**Max**|**Min**|**Max**|
|A|1.050|1.250|0.041|0.049|
|A1|0.000|0.100|0.000|0.004|
|A2|1.050|1.150|0.041|0.045|
|b|0.300|0.500|0.012|0.020|
|c|0.100|0.200|0.004|0.008|
|D|2.820|3.020|0.111|0.119|
|E|2.650|2.950|0.104|0.116|
|E1|1.500|1.700|0.059|0.067|
|e|0.950(BSC)|0.950(BSC)|0.037(BSC)|0.037(BSC)|
|e1|1.800|2.000|0.071|0.079|
|L|0.300|0.600|0.012|0.024|
|θ|0°|8°|0°|8°|


昆泰芯微电子科技有限公司 **13** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**











|Symbol|Dimensions in<br>Millimeters|Col3|Dimensions in<br>Inches|Col5|
|---|---|---|---|---|
|**Symbol**|**Min**|**Max**|**Min**|**Max**|
|A|0.900|1.100|0.035|0.043|
|A1|0.000|0.100|0.000|0.004|
|A2|0.900|1.000|0.035|0.039|
|b|0.150|0.350|0.006|0.014|
|c|0.110|0.175|0.004|0.007|
|D|2.000|2.200|0.079|0.087|
|E|2.150|2.450|0.085|0.096|
|E1|1.150|1.350|0.045|0.053|
|e|0.650 TYP.|0.650 TYP.|0.026 TYP.|0.026 TYP.|
|e1|1.200|1.400|0.047|0.055|
|L|0.300|0.600|0.012|0.024|
|L1|0.525 REF.|0.525 REF.|0.021 REF.|0.021 REF.|
|θ|0°|8°|0°|8°|


昆泰芯微电子科技有限公司 **14** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**











|Symbol|Dimensions in<br>Millimeters|Col3|Dimensions in<br>Inches|Col5|
|---|---|---|---|---|
|**Symbol**|**Min**|**Max**|**Min**|**Max**|
|A|1.350|1.750|0.053|0.069|
|A1|0.100|0.250|0.004|0.010|
|A2|1.350|1.550|0.053|0.061|
|b|0.330|0.510|0.013|0.020|
|c|0.170|0.250|0.006|0.010|
|D|4.700|5.100|0.185|0.200|
|E|5.800|6.200|0.228|0.244|
|E1|3.800|4.000|0.150|0.157|
|e|1.270 TYP.|1.270 TYP.|0.050 TYP.|0.050 TYP.|
|L|0.400|0.800|0.016|0.031|
|θ|0°|8°|0°|8°|


昆泰芯微电子科技有限公司 **15** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**











|Symbol|Dimensions in<br>Millimeters|Col3|Dimensions in<br>Inches|Col5|
|---|---|---|---|---|
|**Symbol**|**Min**|**Max**|**Min**|**Max**|
|A|0.820|1.100|0.032|0.043|
|A1|0.020|0.150|0.001|0.006|
|A2|0.750|0.950|0.030|0.037|
|b|0.250|0.380|0.010|0.015|
|c|0.090|0.230|0.004|0.015|
|D|2.900|3.100|0.114|0.122|
|E|4.750|5.050|0.187|0.199|
|E1|2.900|3.100|0.114|0.122|
|e|0.650 TYP.|0.650 TYP.|0.026 TYP.|0.026 TYP.|
|L|0.400|0.800|0.016|0.031|
|θ|0°|6°|0°|6°|


昆泰芯微电子科技有限公司 **16** **Rev 1.0**


# **KTAx333 系列**

## **零漂移、微功耗、CMOS 运算放大器**











|Symbol|Dimensions in<br>Millimeters|Col3|Dimensions in<br>Inches|Col5|
|---|---|---|---|---|
|**Symbol**|**Min**|**Max**|**Min**|**Max**|
|A|0.700|0.800|0.028|0.031|
|A1|0.000|0.050|0.000|0.002|
|A3|0.203 REF.|0.203 REF.|0.008 REF.|0.008 REF.|
|D|1.900|2.100|0.075|0.083|
|E|1.900|2.100|0.075|0.083|
|D1|0.500|0.700|0.020|0.028|
|E1|1.100|1.300|0.043|0.051|
|K|0.350 REF.|0.350 REF.|0.014 REF.|0.014 REF.|
|b|0.200|0.300|0.008|0.012|
|e|0.500 BSC.|0.500 BSC.|0.020 BSC.|0.020 BSC.|
|L|0.274|0.426|0.011|0.017|


昆泰芯微电子科技有限公司 **17** **Rev 1.0**




</details>

---

## 相关资源

### PDF文档
- [📋 KTAx333_DATASHEET_en.pdf](/pdfs/KTAx333_DATASHEET_en.pdf)
- [📋 KTAx333产品手册.pdf](/pdfs/KTAx333产品手册.pdf)

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

### 其他传感器

- [KTP112 增强版](./KTP112.md) - 同系列产品
- [KTH462N 增强版](./KTH462N.md) - 同系列产品
### 3D霍尔传感器

- [KTH31xx 增强版](./KTH31xx.md) - 推荐3D霍尔传感器
### 磁编码器

- [KTH7801 增强版](./KTH7801.md) - 推荐磁编码器
### 霍尔开关

- [KTH1201 增强版](./KTH1201.md) - 推荐霍尔开关

---
