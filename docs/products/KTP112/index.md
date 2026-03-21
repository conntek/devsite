# KTP112 - 完整技术参考

[返回产品目录](../index.md) | [返回other-sensors分类](../other-sensors/index.md)


## 🧭 页面导航

- 🔙 [返回产品摘要页面](../other-sensors/KTP112.md)
- 📂 [返回其他传感器分类](../other-sensors/)
- 🏠 [返回主页](../index.md)
- 📚 [所有增强版技术参考](./index.md)

---

## 产品概述

**KTP112** 完整技术参考文档，包含所有PDF数据手册的详细内容和技术图片。

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

## 📄 KTP112_CN.pdf

<details>
<summary>点击展开 KTP112_CN.pdf 完整内容</summary>

**1.产品特性**


 工作电源范围：1.8V 至5.5V


 温度工作范围：-40℃至125℃


 超低静态电流：


5.1uA、1Hz转换周期


200nA待机功耗


 全温范围内保持高精度：


-40℃至125℃时为±0.5℃


 可编程温度报警功能


 兼容SMBus，I2C接口


**2.应用**


 医疗温度计


 环境监控和恒温器


 服务器及PC机温度检测


 资产跟踪和冷藏链


 燃气表和热量计


 测试和测量


 热电偶冷端补偿


# KTP112 系列

高性能、低功耗、数字温度传感器


**3.产品概述**


KTP112是一款高精度、低功耗、可替代NTC / PTC


热敏电阻的数字温度传感器，可用于通信、计算机、


消费类电子、环境、工业和仪器仪表应用中的温度


测量。KTP112在-40°C至+125°C的正常工作范围


内，可提供±0.5°C的温度精度，并具有良好的温度


线性度。 KTP112 的额定工作电压范围为


1.8V~5.5V，在整个工作范围内最大静态电流为


5.1µA（测温频率1Hz）。集成在芯片内部的16位


ADC 分辨率低至0.0078 ℃。 KTP112 采用


DFN2*2-6L封装，内置兼容SMBus和I2C接口，同


一条总线上最多可挂载四个从机，并具有SMBus报


警功能。


**4.功能框图**


**5.器件信息**


|器件编号|封装|封装尺寸|湿敏等级|
|---|---|---|---|
|KTP112|DFN2*2-6L|2.00mm x 2.00mm|MSL 3|



昆泰芯微电子科技有限公司 1


**目录**


1. 产品特性................................1


2. 应用....................................1


3. 产品概述................................1


4. 功能框图................................1


5. 器件信息................................1


目录.......................................2


6. 管脚信息................................3


7. 规格....................................3


7.1 绝对最大额定参数...................3


7.2 ESD 评级........................... 4


7.3 推荐的工作条件.....................4


7.4 电参数.............................4


7.5 时序要求...........................5


7.6 典型参数...........................7


8. 详细说明................................8


8.1 总览...............................8


8.2 功能框图...........................9


8.3 功能说明...........................9


8.3.1 上电.........................9


8.3.2 温度结果和限制...............9


8.3.3 串行接口....................10


8.3.4 总线概览....................10


8.3.5 串行总线地址................10


8.3.6 读和写操作..................11


8.3.7 从机模式操作................11


8.3.8 SMBus 警报功能.............. 12


8.3.9 常规响应....................12


8.3.10 高速（HS）模式.............12


8.3.11 超时功能...................12


8.3.12 时序图.....................12


8.4 设备功能模式......................15


8.4.1 连续转换模式................15


8.4.2 单次/转换就绪模式（OS）.....16


8.4.3 恒温器模式（TM）............16


8.4.4 比较器模式（TM=0）..........16


8.4.5 中断模式（TM=1）............17


8.5 配置..............................17


8.5.1 指针寄存器..................17


8.5.2 温度寄存器..................18


8.5.3 配置寄存器..................18


# KTP112 系列

高性能、低功耗、数字温度传感器


8.5.4 上下限值寄存器..............20


9. 应用程序和实现.........................22


9.1 应用程序信息......................22


9.2 典型应用原理图....................22


9.2.1 设计要求....................22


9.2.2 详细设计程序................22


9.2.3 应用程序曲线................23


10. 电源建议..............................24


11. 订货信息..............................24


12. 封装信息..............................25



昆泰芯微电子科技有限公司 2


# KTP112 系列

高性能、低功耗、数字温度传感器


**6.管脚信息**


图 6.1 管脚图

|引脚名称|引脚序号|类型|功能描述|
|---|---|---|---|
|SCL|1|I|串行时钟线；开漏输出；需接上拉电阻|
|GND|2|—|接地端|
|ALERT|3|O|过温报警端；开漏输出；需接上拉电阻|
|ADD0|4|I|地址选择端，可连接V+,GND,SCL,SDA|
|V+|5|I|供电输入端|
|SDA|6|I/O|串行数据线；开漏输出；需接上拉电阻|



**7.规格**


**7.1 绝对最大额定参数**


超过工作自由空气温度范围（除非特别说明） [（1）]

|Col1|Col2|最小值 最大值|单位|
|---|---|---|---|
|电源电压|V+|6|V|
|SCL, ADD0和SDA电压|SCL, ADD0和SDA电压|–0.3<br>6|V|
|ALERT电压|ALERT电压|–0.3<br>((V+) + 0.3) 且≤6|V|
|运行结温，TJ|运行结温，TJ|150|℃|
|贮存温度，Tstg|贮存温度，Tstg|150|℃|



（1）超过绝对最大额定值所列的应力可能会对设备造成永久性损坏。这些仅为应力等级，这并不意味着设备在


这些或在推荐工作条件以外的任何条件下的功能运行。长时间暴露于绝对最大额定条件下可能会影响设备的可


昆泰芯微电子科技有限公司 3


靠性。


**7.2 ESD 评级**

|Col1|Col2|Col3|值|单位|
|---|---|---|---|---|
|V(ESD)|静电放电|人体模型(HBM)|±2000|V|
|V(ESD)|静电放电|充电器件模型(CDM)|±500|V|



**7.3 推荐的工作条件**


超出工作自由空气温度范围（除非另有说明）


# KTP112 系列

高性能、低功耗、数字温度传感器



|Col1|Col2|最小值|标称值|最大值|单位|
|---|---|---|---|---|---|
|V+|电源电压|1.8|3.3|5.5|V|
|VI/O|ALERT,SCL, ADD0和SDA电压|0|3.3|5.5|V|
|TA|工作温度|–40||125|°C|


**7.4 电参数**


在T A = +25°C 、V + = 1.8V to 5.5V 的条件下，除非特别说明。















|参数|Col2|Col3|测试条件|Col5|最小值|典型值|最大值|单位|
|---|---|---|---|---|---|---|---|---|
|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|**数字温度转化器**|
|温度范围|温度范围|温度范围|||–40||+125|°C|
|温度误差精度|温度误差精度|KTP112|1-Hz 转换周期导热焊<br>盘未连接（DFN 封装）|–40°C to 125°C||±0.5|±1|°C|
|直流电源灵敏度|直流电源灵敏度|直流电源灵敏度|单次测量模式，8样本均值计算|单次测量模式，8样本均值计算|0.0156|0.0156|0.0156|℃/V|
|温度分辨率(LSB)|温度分辨率(LSB)|温度分辨率(LSB)|||0.0078|0.0078|0.0078|°C|
|可重复性(1)|可重复性(1)|可重复性(1)|V+=3.3V<br>1-Hz 转换周期|V+=3.3V<br>1-Hz 转换周期|±2|±2|±2|LSB|
|长期稳定性和漂移|长期稳定性和漂移|长期稳定性和漂移|150℃1000小时|150℃1000小时|0.0156|0.0156|0.0156|℃|
|温度循环和迟滞|温度循环和迟滞|温度循环和迟滞|8样本均值计算|8样本均值计算|±2|±2|±2|LSB|
|转化时间|转化时间|转化时间|单次测量模式|单次测量模式||124||ms|
|**数字输入输出**|**数字输入输出**|**数字输入输出**|**数字输入输出**|**数字输入输出**|**数字输入输出**|**数字输入输出**|**数字输入输出**|**数字输入输出**|
|CIN|输入电容|输入电容||||2||pF|
|VIH|输入逻辑高电平|输入逻辑高电平|SCL,SDA|SCL,SDA|0.7*（V+）|||V|
|VIL|输入逻辑低电平|输入逻辑低电平|SCL,SDA|SCL,SDA|||0.3*（V+）|V|


昆泰芯微电子科技有限公司 4


# KTP112 系列

高性能、低功耗、数字温度传感器

|I<br>IN|输入漏电流|Col3|-0.1|Col5|0.1|μA|
|---|---|---|---|---|---|---|
|VOL|SDA和ALERT低电平输出电压|IOL = 10mA|0||0.4|V|
|分辨率|分辨率||16|16|16|Bits|
|转化模式|转化模式|CR1 = 0, CR0 = 0|0.25|0.25|0.25|Conv/s|
|转化模式|转化模式|CR1 = 0, CR0 = 1|1|1|1|1|
|转化模式|转化模式|CR1 = 1, CR0 = 0 (默认)|4|4|4|4|
|转化模式|转化模式|CR1 = 1, CR0 = 1|8|8|8|8|
|超时时间|超时时间|||30|40|ms|
|**供电电源**|**供电电源**|**供电电源**|**供电电源**|**供电电源**|**供电电源**|**供电电源**|
|工作范围|工作范围||1.8|3.3|5.5|V|
|IQ_ACTIVE|转化阶段的静态电流|转化有效，通信关闭||13.5||μA|
|IQ|静态电流|1Hz工作周期，通信关闭，TA=25℃||5.1|||
|ISB|待机电流(4)|通信关闭||3.9||μA|
|ISD|关机电流|通信关闭||0.2||μA|



在空气温度范围内T A = -40℃to 125°C 内，V+= 1.8V to 5.5V，典型规格为T A = +25°C 、V S = 3.3V，（除


非另说明）。

|参数|Col2|测试条件|最小值|典型值|最大值|单位|
|---|---|---|---|---|---|---|
|VPOR|上电-复位的电压阈值|上电||1.6||V|
||掉电监测|掉电||1.1||V|
|tRESET|复位时间|设备复位所需时间||1.8||ms|



（1）可重复性是指在相同条件下连续施加测量温度时再现读数的能力。


（2）长期漂移是通过在结温度为125°C 下进行1000 小时的加速运行寿命测试来确定的。


（3）滞后的定义是温度从室温热→室温→冷→室温的变化中再现温度读数的能力，该测试使用的温度为-40℃，


25℃和125℃。


（4）两次转换之间的静态电流。


**7.5 时序要求**


有关时序图，请参见时序图部分。

|Col1|Col2|Col3|快速模式|Col5|高速模式|Col7|单位|
|---|---|---|---|---|---|---|---|
||||**MIN**|**MAX**|**MIN**|**MAX**|**MAX**|
|ƒ(SCL)|SCL工作频率|V+|0.001|0.4|0.001|2.85|MHz|



昆泰芯微电子科技有限公司 5


# KTP112 系列

高性能、低功耗、数字温度传感器













|t<br>(BUF)|在停止和启动条件之间的无总线时间|见图 8.2|600|Col5|160|Col7|ns|
|---|---|---|---|---|---|---|---|
|t(HDSTA)|重复启动条件后的保持时间。在此周期<br>之后，将生成第一个时钟。|重复启动条件后的保持时间。在此周期<br>之后，将生成第一个时钟。|600||160||ns|
|t(SUSTA)|重复启动条件建立时间|重复启动条件建立时间|600||160||ns|
|t(SUSTO)|停止条件建立时间|停止条件建立时间|600||160||ns|
|t(HDDAT)|数据保持时间|数据保持时间|100|900|25|105|ns|
|t(SUDAT)|数据建立时间|数据建立时间|100||25||ns|
|t(LOW)|SCL时钟低电平周期|V+，见图8.2|1300||210||ns|
|t(HIGH)|SCL时钟高电平周期|见图8.2|600||60||ns|
|tFD|数据下降时间|见图8.2||300||80|ns|
|tRD|数据上升时间|见图8.2||300|||ns|
|tRD|数据上升时间|SCLK ≤100 kHz, 见图8.2||1000|||ns|
|tFC|时钟下降时间|见图8.2||300||40|ns|
|tRC|时钟上升时间|见图8.2||300||40|ns|


昆泰芯微电子科技有限公司 6


# KTP112 系列

高性能、低功耗、数字温度传感器


**7.6 典型参数**


在T A = +25°C 、V+= +3.3V 的油槽中测试，除非特别说明。


昆泰芯微电子科技有限公司 7


# KTP112 系列

高性能、低功耗、数字温度传感器


**8.详细说明**


**8.1 总览**


KTP112 系列设备是数字温度传感器，最适用于热管理和热保护应用。KTP112 系列是SMBus 和I [2] C 接口兼容


的。该设备的工作温度范围为-40℃至125℃。图 8.1 显示了KTP112 系列的方框图。


KTP112 系列中的温度传感器就是芯片本身。热路径贯穿于包装导线和塑料包装上。由于金属的热阻较低，封


装导线提供了主热路径。


昆泰芯微电子科技有限公司 8


# KTP112 系列

高性能、低功耗、数字温度传感器



**8.2 功能框图**


**8.3 功能说明**


**8.3.1 上电**



图 8.1 功能框图



电源电压达到工作范围后，在转换开始之前，器件需要1.5ms 上电时间，在关断模式下也可以编程启动上电。


未进行温度转化前，温度寄存器读出值是0.


**8.3.2 温度结果和限制**


在每次转换结束时，用该转换结果更新温度寄存器。结果寄存器中的数据为二进制补码格式，数据宽度为16


位，分辨率为7.8125m℃。表 8.1 显示了多个可能从温度结果寄存器和相应的十六进制和温度等量中读取二进


制数据的例子。KTP112 系列还具有警报状态标志和警报管脚功能，它们使用存储在下限寄存器和上限寄存器


中的温度限值。温度结果寄存器的数据格式用于写入上限寄存器和下限寄存器的数据。


昆泰芯微电子科技有限公司 9


# KTP112 系列

高性能、低功耗、数字温度传感器


表 8.1 十六位温度数据格式



|温度(°C)|温度寄存器的值 (0.0078125 °C 分辨率)|Col3|
|---|---|---|
|**温度(°C)**|**二进制**|**十六进制**|
|–256|1000 0000 0000 0000|8000|
|–25|1111 0011 1000 0000|F380|
|–0.1250|1111 1111 1111 0000|FFF0|
|–0.0078125|1111 1111 1111 1111|FFFF|
|0|0000 0000 0000 0000|0000|
|0.0078125|0000 0000 0000 0001|0001|
|0.1250|0000 0000 0001 0000|0010|
|1|0000 0000 1000 0000|0080|
|25|0000 1100 1000 0000|0C80|
|100|0011 0010 0000 0000|3200|
|255.9921|0111 1111 1111 1111|7FFF|


**8.3.3 串行接口**


KTP112 系列仅在SMBus 和I2C 接口兼容的总线上作为从属设备运行。通过开漏I/O 线路、SDA 和SCL 引脚


集成了尖峰抑制滤波器和施密特触发器，以最小输入尖峰和总线噪声的影响。KTP112 系列同时支持快速（1kHz


到400kHz）和高速（1kHz 到2.85MHz）模式的传输协议。所有数据字节首先传输MSB。


**8.3.4 总线概览**


启动传输的设备称为主设备，由主设备控制的设备是从设备。总线必须由一个主设备控制，该设备产生串行时


钟（SCL），控制总线访问，并产生启动和停止条件。


为了处理特定的设备，启动一个启动条件，当SCL 引脚较高时，通过将数据线（SDA）从高逻辑级别拉到低逻


辑级别来表示。总线上的所有从位位于时钟上升边缘的从地址字节，最后一个位指示是读操作还是写操作。在


第9 个时钟脉冲中，被寻址的从服务器通过产生确认并降低SDA 引脚来响应主服务器。


然后启动一个数据传输，并通过8 个时钟脉冲发送，然后是一个确认位。在数据传输过程中，当SCL 脚高电平


时，SDA 脚必须保持稳定，因为当SCL 脚高电平时，SDA 脚的任何变化都被解释为启动或停止信号。


当所有数据都被传输后，主控件生成一个STOP 条件，当SCL 脚是高电平时，通过将SDA 从低电平拉到高电


平来指示。


**8.3.5 串行总线地址**


要与设备通信，主设备必须首先通过从地址字节与从设备地址通信。从地址细节由七个地址位和一个指示执行


读或写操作的意图的方向位组成。


昆泰芯微电子科技有限公司 10


# KTP112 系列

高性能、低功耗、数字温度传感器


KTP112 系列有一个地址脚，允许在一个总线上寻址。表 8.2 描述了用于正确连接最多四个设备的引脚逻辑电


平。


表 8.2 地址脚和从地址

|设备双线地址|ADD0脚连接|
|---|---|
|1001000|Ground|
|1001001|V+|
|1001010|SDA|
|1001011|SCL|



**8.3.6 读和写操作**



访问KTP112 系列上的特定寄存器是通过将指针寄存器写入适当的值来完成的。指针寄存器的值是在R/



—
W [位较]



低的从地址字节之后传输的第一个字节。对于KTP112 系列的每隔个写入操作都需要一个指针寄存器的值（参


见图 8.3）


当从KTP112 系列读取时，通过写操作存储在指针寄存器中的最后一个值用于确定通过读取操作读取哪个寄存



器。要更改读取操作的寄存器指针，必须将指针寄存器写入一个新值。这个操作是通过发出一个R/



—
W [位数较低]



的从属地址字节，然后是指针寄存器字节来完成的。不需要提供其他数据。然后，主服务器可以生成一个启动



条件，并发送R/



—
W [位高的从地址字节，以启动读取命令。有关次序列的详细信息，请参阅][图] [8.4][。如果需要从]



同意寄存器重复读取，则不需要连续发送指针寄存器字节，因为KTP112 系列保留指针寄存器值，直到下一个


写操作更改该值。


寄存器字节首先发送最重要的字节，然后是最不重要的字节。


**8.3.7 从机模式操作**


KTP112 系列可以作为从接收机或从发射机进行操作。作为一个从属设备，KTP112 系列从不驱动SCL 线。


**8.3.7.1 从机接收机模式**



主节点传输的第一个字节是R/



—
W [位低的从地址。然后，KTP112 系列确认收到了一个有效的地址。由主服务器]



传输的下一个字节是指针寄存器。然后，KTP112 系列确认接收到指针寄存器字节。下一个字节或多个字节被


写入由指针寄存器寻址的寄存器。KTP112 系列确认接受到每个数据字节。主服务器可以通过生成启动或停止


条件来终止数据传输。


**8.3.7.2 从机发射机模式**



主节点传输的第一个字节是R/



—
W [位低的从地址。从地址接收到一个有效的从地址。下一个字节由从属节点传输，]



并且是由指针寄存器指示的寄存器中最重要的字节。主服务器确认接受到该数据字节。从服务器传输的下一个


字节是最重要的字节。主服务器确认接受到该数据字节。主服务器可以通过生成对接受到任何数据字节的不确


认或通过生成启动或停止条件来终止数据传输。


昆泰芯微电子科技有限公司 11


# KTP112 系列

高性能、低功耗、数字温度传感器


**8.3.8 SMBus 警报功能**


KTP112 系列支持SMBus 警报功能。当KTP112 系列处于中断模式（TM=1）时，警报引脚可以作为SMBus


警报信号连接起来。当主线感知到即警报线上存在警报条件时，主线会向总线发送SMBus 警报命令


（00011001）。如果警报脚有效，则该设备将确认SMBus 警报命令，并通过返回SDA 行上的从属地址进行


响应。从地址字节的第八位（LSB）表示警报条件是由温度超过T （HIGH） 或低于T （LOW） 引起的。如果温度大于


T （HIGH） ，则LSB 为高，如果温度小于T （LOW） ，则LSB 为低。有关此序列的详情信息，则参见图 8.5 部分。


如果总线上的多个设备响应SMBus 警报命令，则在SMBus 警报命令的从地址部分器件的仲裁将确定哪个设备


清除该设备的警报状态。双线地址最低的设备将赢得仲裁。如果KTP112 系列赢得仲裁。如果KTP112 系列警


报脚将变成无效状态；如果KTP112 系列输掉仲裁，则KTP112 系列警报引脚仍处于有效状态。


**8.3.9 常规响应**


如果第8 位为0，则KTP112 系列响应一个双线通用调用地址（0000000）。该设备确认通用调用地址，并响


应第二个字节中的命令。如果第二个字节为00000110，则KTP112 系列内部寄存器将被重置为上电初始值。


KTP112 系列不支持通用地址获取命令。


**8.3.10 高速（HS）模式**


为了使双线总线在400kHz 以上的频率下运行，主设备必须发出一个Hs 模式主码（0000 1xxx）作为启动条件


后的第一个字节，以便将总线切换到高速运行。KTP112 系列不承认这个字节，但切换SDA 和SCL 引脚上的输


入过滤器和SDA 引脚上的输出过滤器，以在Hs 模式下运行，从而允许高达2.85MHz 的传输。在发出高速模


式主代码发出后，主传输一个双线从地址以启动数据传输操作。总线继续在Hs 模式下运行，直到总线上发出


停止状态。在接收到停止条件后，KTP112 系列将输入和输出滤波器切换回快速模式操作。


**8.3.11 超时功能**


如果SCL 引脚在启动和停止条件之间保持在较低水平30ms（典型），KTP112 系列将重置串行接口。如果SCL


引脚将被拉到较低的位置并等待来自主机控制器的启动条件，那么KTP112 系列就会释放SDA 线。为了避免激


活超时功能，为SCL 工作频率保持至少1kHz 的通信速度。


**8.3.12 时序图**


KTP112系列是SMBus和I [2] C接口兼容的。图 8.2至图 8.5描述了KTP112系列上的各种操作。图 8.2的参数在时


序要求中定义。总线定义为：


**Bus Idle** （总线空闲）：SDA和SCL线保持高电平。


**Start Data Transfer** （启动数据传输）：当SCL线是高电平时，SDA线状态从高到低的变化定义了启动条件。


每次数据传输都以一个启动条件开始。


**Stop Data Transfer** （停止数据传输）：当SCL线是高电平时，SDA线状态从低到高的变化定义了停止条件。


昆泰芯微电子科技有限公司 12


# KTP112 系列

高性能、低功耗、数字温度传感器


每次数据传输都以重复的启动条件或停止条件终止。


**Data Transfer** （数据传输）：在启动条件和停止条件之间传输的数据字节数不受限制，并由主设备决定。KTP112


系列也可以用于单个字节的更新。若要仅更新MS字节，请通过在总线上发出启动或终止通信来终止通信。


**Acknowledge** （确认）：每个接收设备在通信时，必须生成一个确认位。在确认时钟脉冲期间必须下拉SDA


线，使SDA线在确认时钟脉冲的高周期内SDA线稳定在低。必须考虑到建立时间和保持时间。在主接收上，主


接收在从传输的最后一个字节上生成一个不确认（“1”），可以表示数据传输的终止。


**8.3.12.1 I** **[2]** **C时序图**


图 8.2 I2C 时序图


图 8.3 写寄存器时序图


昆泰芯微电子科技有限公司 13


# KTP112 系列

高性能、低功耗、数字温度传感器


图 8.4 读寄存器时序图


图 8.5 SMBus ALERT 时序图


昆泰芯微电子科技有限公司 14


# KTP112 系列

高性能、低功耗、数字温度传感器


**8.4 设备功能模式**


**8.4.1 连续转换模式**


KTP112系列的默认值是连续转换模式。在连续模式下，ADC执行连续的温度转换，并将每个结果存储到温度


寄存器中，覆盖之前转换的结果。转换速率位CR1和CR0将KTP112系列配置为转换速率的0.25Hz、1Hz、4Hz


或8Hz。KTP112系列的典型转换时间为124ms。为了实现不同的转换率，KTP112系列进行转换，然后断电，


等待CR1和CR0设置的适当延迟。表 8.3列出了CR1和CR0的设置。


表 8.3 转换率设置

|CR1|CR0|转化速率|
|---|---|---|
|0|0|0.25 Hz|
|0|1|1 Hz|
|1|0|4 Hz (默认)|
|1|1|8 Hz|



在通电或通用重置后，KTP112 系列将立即开始转换，如图 8.6 所示。第一个结果在124ms 之后（典型）。转


换过程中的有效静态电流为13.7μA（典型值为+27℃）。延迟期间的静态电流为3.9μA（典型值为+27℃）。


图 8.6 转换开始


昆泰芯微电子科技有限公司 15


# KTP112 系列

高性能、低功耗、数字温度传感器


可以使用公式1 来计算连续模式下设备的平均功耗：


~~（~~ 公式 1）

周期转化时间


**8.4.2 单次/转换就绪模式（OS）**


KTP112 系列采用了单次温度测量模式。当设备处于关闭模式时，向OS 位写入一个1 将开始一次温度转换。


在转换过程中，OS 位读取为0。在单次转换完成后，设备返回到关机状态。转换后，OS 位读取为1。当不需


要连续的温度监测时，此特性可用于降低KTP112 系列的功耗。由于转换时间较短，KTP112 系列可以实现较


高的转换率。单次转换通常发生在124ms，一次读取可以发生在不到20μs。当使用单次模式时，可以实现每


秒最多8 次的转换。


图 8.7 单次测量模式时序图


**8.4.3 恒温器模式（TM）**


恒温器模式位指示设备是在比较器模式（TM=0）还是中断模式（TM=1）下运行。


**8.4.4 比较器模式（TM=0）**


在比较器模式（TM=0）中，当温度等于或超过T （HIGH） 寄存器的值时，警报脚被激活，并保持有效状态，直到


昆泰芯微电子科技有限公司 16


# KTP112 系列

高性能、低功耗、数字温度传感器


温度低于T （LOW） 寄存器的值。有关比较器模式的更多信息，请参阅上限和下限寄存器部分。


**8.4.5 中断模式（TM=1）**


在中断模式（TM=1）中，当温度超过T （HIGH） 寄存器或低于T （LOW） 寄存器时，警报脚有效。当主机控制器读


取温度寄存器时，警报脚将被清除。有关中断模式的更多信息，请参阅上限和下限寄存器部分。


**8.5 配置**


**8.5.1 指针寄存器**


图 8.8显示了KTP112系列的内部寄存器结构。该设备的8位指针寄存器用于处理给定的数据寄存器。指针寄存


器使用这两个LSB（参见表8.10）来标识哪些数据寄存器必须响应读取或写命令。P1/P0的通电复位值为“00”。


默认情况下，KTP112系列在通电时读取温度。


图 8.8 内部寄存器结构


表 8.4列出了KTP112系列中可用的寄存器的指针地址。表 8.5列出了指针寄存器字节的位。在写命令中，字节


P2到P7必须始终为0。


昆泰芯微电子科技有限公司 17


# KTP112 系列

高性能、低功耗、数字温度传感器


表 8.4 指针地址

|P1|P0|寄存器|
|---|---|---|
|0|0|温度寄存器（只读）|
|0|1|配置寄存器(读/写)|
|1|0|TLOW寄存器(读/写)|
|1|1|THIGH寄存器(读/写)|



表 8.5 指针寄存器字节

|P7|P6|P5|P4|P3|P2|P1|P0|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|Register Bits|Register Bits|



**8.5.2 温度寄存器**


KTP112 系列的温度寄存器被配置为16 位只读寄存器必须读取两个字节才能获得数据，并列在表 8.6 和表 8.7


中。带符号位的16 位数据用于指示温度。


表 8.6 温度寄存器的高字节

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|T15|T14|T13|T12|T11|T10|T9|T8|



表 8.7 温度寄存器的低字节

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|2|T7|T6|T5|T4|T3|T2|T1|T0|



**8.5.3 配置寄存器**


配置寄存器是一个16位的读/写寄存器，用于存储控制温度传感器的工作模式的位。读/写操作首先执行MSB。


表 8.8列出了配置寄存器的格式、上电默认值。


表 8.8 配置和上电默认值

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|OS|R1|R0|F1|F0|POL|TM|SD|
|1|0|1|1|0|0|0|0|0|
|2|CR1|CR0|AL|EM|0|0|0|0|
|2|1|0|1|0|0|0|0|0|



**8.5.3.1 关闭模式（SD）**


关闭模式：通过关闭除串行接口以外的所有设备电路来节省最大功率，将电流消耗减少到通常小于0.25μA。当


昆泰芯微电子科技有限公司 18


# KTP112 系列

高性能、低功耗、数字温度传感器


SD位=1时，启用关闭模式；当前转换完成时，设备关闭。当SD位=0时，设备保持连续转换状态。


**8.5.3.2 恒温器模式（TM）**


恒温器模式位指示设备是否在比较器模式（TM=0）或中断模式（TM=1）下运行。


**8.5.3.3 极性（POL）**


极性位允许用户调整ALERT引脚输出的极性。如果POL位设置为0时，ALERT引脚变为低电平有效。当POL位设


置为1时，ALERT引脚变为高电平有效并且ALERT引脚的状态翻转。


图 8.9 输出传递函数图


**8.5.3.4 故障队列（F1/F0）**


当测量的温度超过T HIGH和 T LOW 寄存器中设置的用户定义限制时，存在故障条件。此外，还可以使用故障队列对


生成警报所需的故障条件数进行编程。提供故障队列是为了防止由于环境噪声而产生的错误警报。故障队列需


要连续的故障测量，以触发警报能。表 8.9列出了可能被变成为在设备中触发警报条件的测量故障的数量。


昆泰芯微电子科技有限公司 19


# KTP112 系列

高性能、低功耗、数字温度传感器


表 8.9 KTP112 系列故障设置

|F1|F0|连续错误数|
|---|---|---|
|0|0|1|
|0|1|2|
|1|0|4|
|1|1|6|



**8.5.3.5 单次模式（OS）**


当设备处于关闭模式时，向操作系统位写入一个1将开始一次温度转换。在转换过程中，操作系统位读取为0。


在单次转换完成后，设备返回到关机状态。有关一次性转换模式的更多信息，请参见单次/转换就绪模式（OS）


部分。


**8.5.3.6 警报（AL）**


AL位是一个只读函数。读取AL位就提供了有关比较器模式状态的信息。POL位的状态反转了从AL位返回的数据


的极性。当POL位等于0时，AL位读取为1，直到温度等于或超过已编程的连续故障数的T HIGH ，从而导致AL位


读取为0。AL位继续读取为0，直到温度降至程序中的连续故障数T LOW 以下，然后再次读取为1。TM位的状态并


不影响AL位的状态。


**8.5.4 上下限值寄存器**


温度限值以与温度结果相同的格式存储在T HIGH和 T LOW 寄存器中，并在每次装换时将他们的值与温度结果进行比


较。比较的结果驱动ALERT管脚的表现，它作为比较器输出或中断进行操作，并由配置寄存器中的TM位设置。


在比较器模式（TM=0）中，当温度等于或超过T HIGH 寄存器中的值时，ALERT管脚变得有效，并根据故障位F1


和F0生成连续的故障数。ALERT管脚保持有效直到温度低于相同的故障数的标定的T LOW 值。


在中断模式（TM=1）中，当温度等于或超过T HIGH 寄存器中的值时时（如表 8.8所示）。在发生任何寄存器的


读取操作，或设备成功响应SMBus警报响应地址之前，ALERT引脚一直保持有效状态。如果设备处于关闭模式，


ALERT引脚也会被清除。当ALERT引脚被清除时，只有当温度低于T LOW 时，它才会再次被激活，并且一直保持


激活状态，直到通过任何寄存器的读取操作或对SMBus警报响应地址的成功响应被清除。当ALERT引脚被清除


时，上述循环将重复，当温度等于或超过T HIGH 时，ALERT引脚将被激活。还可以通过使用通用调用重置命令重


置设备来清除ALERT引脚。此操作还将清除设备中内部寄存器的状态，将设备返回到比较器模式（TM=0）。


这两种操作模式都如图 8.9所示。表 8.10和表 8.11列出了T HIGH 和T LOW 寄存器的格式。T HIGH和 T LOW 的上电复位


值为：


 - T HIGH = +80°C


 - T LOW = +75°C


T HIGH 和T LOW 的数据格式与温度寄存器相同。


昆泰芯微电子科技有限公司 20


# KTP112 系列

高性能、低功耗、数字温度传感器


表 8.10 T HIGH 寄存器的高字节和低字节

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|H15|H14|H13|H12|H11|H10|H9|H8|
||||||||||
|**BYTE**|**D7**|**D6**|**D5**|**D4**|**D3**|**D2**|**D1**|**D0**|
|2|H7|H6|H5|H4|H3|H2|H1|H0|



表 8.11 T LOW 寄存器的高字节和低字节

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|L15|L14|L13|L12|L11|L10|L9|L8|
||||||||||
|**BYTE**|**D7**|**D6**|**D5**|**D4**|**D3**|**D2**|**D1**|**D0**|
|2|L7|L6|L5|L4|L3|L2|L1|L0|



昆泰芯微电子科技有限公司 21


# KTP112 系列

高性能、低功耗、数字温度传感器


**9.应用程序和实现**


**9.1 应用程序信息**


KTP112 系列用于测量设备安装板位置的PCB 温度。可编程地址选项允许在单个串行总线上的监控电路板上的


多达四个位置。


**9.2 典型应用原理图**


图 9.1 典型连接


**9.2.1 设计要求**


KTP112系列需要在SCL、SDA和警报脚上安装上拉电阻。上拉电阻的推荐值为5kΩ。在某些应用中，上拉电阻


可以低于或高于5kΩ，但不能低于500Ω，且不能超过任何这些引脚上的10mA电流。建议在电源上安装一个0.1


μF的旁路电容器，如图 9.1所示。SCL和SDA线可以通过上拉电阻被拉上至等于或高于V+的电源。要在总线上


配置四个不同的地址之一，请将ADD0引脚连接到GND、V+、SDA或SCL引脚。


**9.2.2 详细设计程序**


将设备放置在必须监测的热源附近，以适当的布局，以实现良好的热耦合。这种位置确保在最短的时间间隔内


昆泰芯微电子科技有限公司 22


# KTP112 系列

高性能、低功耗、数字温度传感器


捕获温度变化。为了在需要空气或表面温度测量的应用中保持准确定，请注意将包装和导线与环境空气温度隔


离。一种导热性粘合剂有助于实现准确的表面温度测量。


KTP112系列是一个非常低功率的设备，并在电源总线上产生非常低的噪声。在KTP112系列的V+引脚上应用


RC滤波器可以进一步减少该设备可能传播到其他组件的任何噪声。图 9.2中的R （F） 必须小于5kΩ，而C （F） 必


须大于10nF。


图 9.2 降噪技术


**9.2.3 应用程序曲线**


图 9.3显示了KTP112系列在室温（26℃）下浸入100℃油浴中的阶跃响应。时间常数，或输出达到输入步长的


63%的时间，为3.1s。时间常数的结果取决于KTP112系列所安装的印刷电路板（PCB）。在这个测试中，KTP112


系列被焊接到一个两层PCB上，尺寸为1.5英寸1.5英寸。


昆泰芯微电子科技有限公司 23


# KTP112 系列

高性能、低功耗、数字温度传感器


图 9.3 温度阶跃响应


**10.电源建议**


KTP112 系列的电源范围为1.8 至5.5V。该设备优化为3.3V 运行，但可以在整个电源运行，但可以在整个电源


范围内准确测量温度。一个电源旁路电容器需要正常运行。将此电容器尽可能靠近设备的电源和接地引脚。该


店员旁路电容的典型值为0.1μF。带有噪声或高阻抗电源的应用程序可能需要额外的解耦电容来抑制电源噪声。


**11.订货信息**

|型号|封装形式|MSL|Peak Temp(℃)|OP Temp(℃)|Marking|
|---|---|---|---|---|---|
|KTP112-DZ6|DFN2*2-6L|Level-3|260|-40-125||



昆泰芯微电子科技有限公司 24


# KTP112 系列

高性能、低功耗、数字温度传感器


**12.封装信息**


图 12.1 DFN2*2-6L 封装形状与尺寸


昆泰芯微电子科技有限公司 25




</details>

---

## 📄 KTP112_Datasheet_EN.pdf

<details>
<summary>点击展开 KTP112_Datasheet_EN.pdf 完整内容</summary>

# KTP112 Series

## High Performance, Low Power Digital Temperature Sensor IC

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


KTP112 Series

|Region|Contact Information|
|---|---|
|Overseas|Email: sales.global@conntek.com.cn|
|China|Email: sales@conntek.com.cn|



3 of 24


## Table of Contents

**1 Product Features** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **6**


**2 Applications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **6**


**3 Product Overview** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **6**


**4 Functional Block Diagram** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **7**


**5 Device Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **7**


**6 Pin Out Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **7**


**7 Specifications** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **8**


**7.1** Absolute Maximum Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
**7.2** ESD Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
**7.3** Recommended Operating Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

**7.4** Electrical Characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**7.4.1** Digital Temperature Converter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**7.4.2** Digital Input/Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**7.4.3** Power Supply. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
**7.5** Timing Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

**7.6** Measurement Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10


**8 Detailed Description** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **11**


**8.1** Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

**8.2** Functional Block Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
**8.3** Functional Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


**8.3.1** Power-Up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


**8.3.2** Temperature Result and Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


**8.3.3** Serial Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


**8.3.4** Bus Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


**8.3.5** Serial Bus Address . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


**8.3.6** Read and Write Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


**8.3.7** Slave Mode Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**8.3.8** SMBus Alert Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**8.3.9** General Call Response. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**8.3.10** High-Speed (HS) Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**8.3.11** Timeout Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**8.3.12** Timing Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

**8.4** Device Functional Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


**8.4.1** Continuous Conversion Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


**8.4.2** One-Shot/Conversion Ready Mode (OS) . . . . . . . . . . . . . . . . . . . . . . . 17


**8.4.3** Thermostat Mode (TM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


KTP112 Series


**8.4.4** Comparator Mode (TM=0) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


**8.4.5** Interrupt Mode (TM=1). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
**8.5** Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


**8.5.1** Pointer Register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


**8.5.2** Temperature Register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


**8.5.3** Configuration Register. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


**8.5.4** Upper and Lower Limit Registers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21


**9 Applications and Implementation** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **21**


**9.1** Application Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
**9.2** Typical Application Schematic. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
**9.3** Design Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
**9.4** Detailed Design Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
**9.5** Application Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23


**10 Power Supply Recommendations** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **23**


**11 Ordering Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **24**


**12 Package Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **24**


5 of 24


KTP112 Series

## 1 Product Features

### • [Operating power supply range:][ 1] [.] [8] [V] [ to][ 5] [.] [5] [V] • [Temperature operating range:] [ −] [40] [�] [C] [ to][ 125] [�] [C] • [Ultra-low standby current:] – [5] [.] [1] [µA] [,][ 1] [Hz] [ conversion cycle] – [200] [nA] [ standby power consumption] • [High accuracy maintained over the entire temperature range:] – [±] [0] [.] [5] [�] [C] [ from] [ −] [40] [�] [C] [ to][ 125] [�] [C] • [Programmable temperature alarm function] • [Compatible with SMBus and I] [2] [C interfaces]

## 2 Applications

### • [Medical thermometers] • [Environmental monitoring and thermostats] • [Server and PC temperature detection] • [Asset tracking and cold supply chain] • [Gas meters and heat meters] • [Testing and measurement] • [Thermocouple cold junction compensation]

## 3 Product Overview


The KTP112 is a high-precision, low-power digital temperature sensor
that can replace NTC/PTC thermistors and can be used for temperature
measurement in communications, computers, consumer electronics, environmental, industrial, and instrumentation applications. The KTP112
provides an accuracy of _±_ 0 _._ 5 � _C_ over a normal operating range of _−_ 40 � _C_
to +125 � _C_ and has good temperature linearity. The KTP112 operates
over a voltage range of 1 _._ 8 _V_ to 5 _._ 5 _V_, with a maximum standby current of
5 _._ 1 _µA_ (temperature measurement frequency 1 _Hz_ ) across the entire op
�
erating range. The internal 16-bit ADC resolution is as low as 0 _._ 0078 _C_ .
The KTP112 is packaged in a DFN2×2-6L package with integrated SMBus
and I [2] C interfaces, supporting up to four slaves on the same bus with
SMBus alarm function.


6 of 24


KTP112 Series

## 4 Functional Block Diagram


Figure 1: Functional Block Diagram of KTP112

## 5 Device Information

|Part Number|Package|Package Size|Moisture Sensitivity Level|
|---|---|---|---|
|KTP112|DFN2×2-6L|2_._00_mm ×_ 2_._00_mm_|MSL 3|


## 6 Pin Out Information


Figure 2: Pin Diagram of KTP112


7 of 24


KTP112 Series

|Pin Name|Pin Number|Type|Description|
|---|---|---|---|
|SCL<br>GND<br>ALERT<br>ADD0<br>V+<br>SDA|1<br>2<br>3<br>4<br>5<br>6|I<br>-<br>O<br>I<br>I<br>I/O|Serial clock line; open-drain output; requires pull-<br>up resistor<br>Ground<br>Over-temperature alarm output; open-drain out-<br>put; requires pull-up resistor<br>Address selection pin, can be connected to V+,<br>GND, SCL, SDA<br>Power supply input<br>Serial data line; open-drain output; requires pull-<br>up resistor|


## 7 Specifications


7.1 Absolute Maximum Ratings


Stresses beyond those listed under Absolute Maximum Ratings may
cause permanent damage to the device. These are stress ratings only
and functional operation of the device at these or any other conditions
beyond those indicated under Recommended Operating Conditions is
not implied. Exposure to absolute maximum rating conditions for extended periods may affect device reliability.

|Parameter|Min|Max|
|---|---|---|
|Power supply voltage,_ V_ +<br>SCL, ADD0 and SDA voltage<br>ALERT voltage<br>Operating junction temperature,_ TJ_<br>Storage temperature,_ Tstg_|-<br>_−_0_._3_V_<br>_−_0_._3_V_<br>-<br>-|6_V_<br>6_V_<br>((_V_ +) + 0_._3_V_ ), and_ ≤_6_V_<br>150°_C_<br>150°_C_|



7.2 ESD Ratings

|Parameter|Value|
|---|---|
|ESD HBM (Human Body Model)<br>ESD CDM (Charged Device Model)|_±_2000_V_<br>_±_500_V_|



7.3 Recommended Operating Conditions


Beyond the operating free-air temperature range (unless otherwise noted).

|Symbol|Parameter|Min|Typical|Max|
|---|---|---|---|---|
|_V_ +<br>_VI_/_O_<br>_TA_|Power supply voltage<br>ALERT, SCL, ADD0, and SDA voltage<br>Operating temperature|1_._8_V_<br>0_V_<br>_−_40°_C_|3_._3_V_<br>3_._3_V_<br>-|5_._5_V_<br>5_._5_V_<br>125°_C_|



8 of 24


KTP112 Series


7.4 Electrical Characteristics


Under the conditions of _T_ _A_ = +25 � _C_ and _V_ + = 1 _._ 8 _V_ to 5 _._ 5 _V_, unless
otherwise noted.


7.4.1 Digital Temperature Converter













|Parameter|Test Conditions|Min|Typical|Max|
|---|---|---|---|---|
|Temperature range<br>Temperature accuracy<br>DC power supply sensitivity<br>Temperature resolution (LSB)<br>Reproducibility1<br>Long-term stability and drift2<br>Temperature cycle and hysteresis3<br>Conversion time|-<br>1_Hz_ conversion cycle, ther-<br>mal pad not connected (DFN<br>package)._ −_40°_C −_125°_C_<br>Single measurement mode,<br>8-sample average<br>-<br>_V_ + = 3_._3_V_, 1_Hz_ conversion<br>cycle<br>150°_C_, 1000 hours<br>8-sample average<br>Single measurement mode|_−_40°_C_<br>-<br>-<br>-<br>-<br>-<br>-<br>-|-<br>_±_0_._5°_C_<br>0_._0156°_C_/_V_<br>0_._0078°_C_<br>_±_2_LSB_<br>0_._0156°_C_<br>_±_2_LSB_<br>124_ms_|125°_C_<br>_±_1°_C_<br>-<br>-<br>-<br>-<br>-<br>-|


1 Reproducibility is the ability to reproduce the reading when the same temperature is
applied continuously under the same conditions. [2] Long-term drift is determined through

�
an accelerated life test of 1000 hours at a junction temperature of 125 _C_ . [3] The definition
of hysteresis here is the ability to reproduce the temperature reading during temperature
changes from room temperature to hot, back to room temperature, to cold, and then back

� � �
to room temperature. The temperatures used for this test are _−_ 40 _C_, 25 _C_, and 125 _C_ .


7.4.2 Digital Input/Output

|Parameter|Test Conditions|Min|Typical|Max|
|---|---|---|---|---|
|_CIN_, input capacitance<br>_VIH_, input logic high voltage<br>_VIL_, input logic low voltage<br>_IIN_, input leakage current<br>_VOL_, SDA and ALERT low-level output voltage|-<br>SCL, SDA<br>SCL, SDA<br>-<br>_IOL_ = 10_mA_|-<br>0_._7_ ×_ (_V_ +)V<br>-<br>_−_0_._1_µA_<br>0V|2pF<br>-<br>-<br>-<br>-|-<br>-<br>0_._3_ ×_ (_V_ +)V<br>0_._1_µA_<br>0.4V|
|Resolution<br>Conversion mode<br>Timeout|-<br>CR1=0, CR0=0<br>CR1=0, CR0=1<br>CR1=1, CR0=0 (default)<br>CR1=1, CR0=1<br>-|-<br>-<br>-<br>-<br>-<br>-|16 Bits<br>0.25 Conv/s<br>1 Conv/s<br>4 Conv/s<br>8 Conv/s<br>30ms|-<br>-<br>-<br>-<br>-<br>40ms|



7.4.3 Power Supply

|Parameter|Test Conditions|Min|Typical|Max|
|---|---|---|---|---|
|Operating voltage range<br>_IQ_ACT IV E_, quiescent current during conversion<br>_IQ_, quiescent current<br>_ISB_, standby current4<br>_ISD_, shutdown current<br>_VP OR_, power-on-reset voltage threshold<br>_VP DD_, power-down detection<br>_tRESET_, reset time|-<br>Effective conversion, communication off<br>1Hz working frequency, communication off,_ TA_ = 25°_C_<br>Communication off<br>Communication off<br>Power-up<br>Power-down<br>Time for device reset|1_._8_V_<br>-<br>-<br>-<br>-<br>-<br>-<br>-|3_._3_V_<br>13_._5_µA_<br>5_._1_µA_<br>3_._9_µA_<br>0_._2_µA_<br>1_._6_V_<br>1_._1_V_<br>1_._8_ms_|5_._5_V_<br>-<br>-<br>-<br>-<br>-<br>-<br>-|



9 of 24


KTP112 Series


4 Standby current between conversions.


Within the free-air temperature range _T_ _A_ = _−_ 40 � _C_ to 125 � _C_, _V_ + = 1 _._ 8 _V_ to 5 _._ 5 _V_, typical
specifications at _T_ _A_ = +25 � _C_ and _V_ + = 3 _._ 3 _V_ (unless otherwise noted).


7.5 Timing Requirements


Refer to the Timing Diagram Section:?? for details on timing diagrams.

|Parameter|Test Conditions|Fast Mode<br>Min Max|Col4|High-Speed Mode<br>Min Max|Col6|Unit|
|---|---|---|---|---|---|---|
|_fSCL_, SCL clock frequency<br>_tBUF_, bus free time between a STOP and START condition<br>_tHDST A_, hold time after (repeated) START condition<br>_tSUST A_, setup time for a repeated START condition<br>_tSUST O_, setup time for STOP condition<br>_tHDDAT_, data hold time<br>_tSUDAT_, data setup time<br>_tLOW_, SCL clock low voltage period<br>_tHIGH_, SCL clock high voltage period<br>_tF D_, data fall time<br>_tRD_, data rise time<br>_tF C_, fall time of SCL signals<br>_tRC_, rise time of SCL signals|V+<br>Refer to Fig. 7<br>Refer to Fig. 7<br>Refer to Fig. 7<br>Refer to Fig. 7<br>Refer to Fig. 7<br>Refer to Fig. 7<br>V+, Refer to Fig.<br>7<br>Refer to Fig. 7<br>Refer to Fig. 7<br>Refer to Fig. 7<br>_SCLK ≤_100<br>kHz, refer to Fig.<br>7<br>Refer to Fig. 7<br>Refer to Fig. 7|0.001<br>600<br>600<br>600<br>600<br>100<br>100<br>1300<br>600<br>-<br>-<br>-<br>-<br>-|0.4<br>-<br>-<br>-<br>-<br>900<br>-<br>-<br>-<br>300<br>300<br>1000<br>300<br>300|0.001<br>160<br>160<br>160<br>160<br>25<br>25<br>210<br>60<br>-<br>-<br>-<br>-<br>-|2.85<br>-<br>-<br>-<br>-<br>105<br>-<br>-<br>-<br>80<br>-<br>-<br>40<br>40|MHz<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns|



7.6 Measurement Curves


Tested in an oil bath at _T_ _A_ = +25 � _C_, _V_ + = +3 _._ 3 _V_, unless otherwise noted.


Figure 3: 1Hz Conversion Cycle, DFN Package, Temperature Error vs Temperature


10 of 24


KTP112 Series


Figure 4: Data Distribution (LSB) vs Population (%)


�
Figure 5: 25 C, _V_ + = 3 _._ 3 _V_, Effective Conversion Time Variation Percentage vs
Temperature

## 8 Detailed Description


8.1 Overview


The KTP112 series devices are digital temperature sensors best suited for thermal management and thermal protection applications. The KTP112 series is compatible with SMBus

� �
and I [2] C interfaces. The operating temperature range is _−_ 40 _C_ to 125 _C_ . Figure 6 shows
the block diagram of the KTP112 series.


The temperature sensor in the KTP112 series is the chip itself. The thermal path runs
through the package leads and the plastic packaging. Due to the low thermal resistance
of the metal, the package leads provide the primary thermal path.


11 of 24


KTP112 Series


8.2 Functional Block Diagram


Figure 6: Functional Block Diagram


8.3 Functional Description


8.3.1 Power-Up


After the power supply voltage reaches the operating range, the device requires a 1 _._ 5 _ms_
power-up time before conversion starts, and it can be programmed to initiate power-up in
shutdown mode. Before temperature conversion, the temperature register reads 0.


8.3.2 Temperature Result and Limits


At the end of each conversion, the result is updated in the temperature register. The data
in the result register is in binary complement format, with a data width of 16 bits and a

�
resolution of 7 _._ 8125 _m_ _C_ . Table 1 shows several examples of binary data that can be read
from the temperature result register and the corresponding hexadecimal and temperature
equivalents. The KTP112 series also has alarm status flags and an alert pin function, which
use temperature limit values stored in the lower and upper limit registers. The data format of the temperature result register is used for writing data to the upper and lower limit
registers.


Table 1: 16-bit Temperature Data Format of the values in the temperature register with the

�
resolution of 7 _._ 8125 _m_ _C_

|Temperature (°C)|Binary|Hexadecimal|
|---|---|---|
|_−_256<br>_−_25<br>_−_0_._1250<br>_−_0_._0078125<br>0<br>0_._0078125<br>0_._1250<br>1<br>25<br>100<br>255_._9921|1000000000000000<br>1111001110000000<br>1111111111110000<br>1111111111111111<br>0000000000000000<br>0000000000000001<br>0000000000010000<br>0000000010000000<br>0000110010000000<br>0011001000000000<br>0111111111111111|8000<br>_F_380<br>_FFF_0<br>_FFFF_<br>0000<br>0001<br>0010<br>0080<br>0_C_80<br>3200<br>7_FFF_|



12 of 24


KTP112 Series


8.3.3 Serial Interface


The KTP112 series operates only as a slave device on SMBus and I [2] C interface-compatible
buses. Integrated spike suppression filters and Schmitt triggers on the open-drain I/O
lines, SDA and SCL pins, minimize input spikes and bus noise effects. The KTP112 series
supports both Fast Mode (1kHz to 400kHz) and High-Speed Mode (1kHz to 2.85MHz) transfer protocols. All data bytes are transmitted MSB first.


8.3.4 Bus Overview


The device that initiates transmission is called the master, and the devices under the master’s control are slaves. The bus must be controlled by a single master device that generates the serial clock (SCL), controls bus access, and generates start and stop conditions.


To address a specific device, a start condition is initiated by pulling the data line (SDA)
from high to low when the SCL pin is high. All slave bits on the bus are at the rising edge
of the clock. The last bit indicates whether a read or write operation is intended. On the
ninth clock pulse, the addressed slave responds to the master by generating an acknowledgment and pulling the SDA pin low.


Data transmission is then initiated and sent over eight clock pulses followed by an acknowledgment bit. During data transmission, the SDA pin must remain stable while the
SCL pin is high because any changes on the SDA pin while the SCL pin is high are interpreted as start or stop signals.


When all data has been transmitted, the master generates a STOP condition by pulling the
SDA pin from low to high while the SCL pin is high.


8.3.5 Serial Bus Address


To communicate with a device, the master must first address it via a slave address byte.
The slave address consists of seven address bits and a direction bit indicating the operation to be performed (read or write).


The KTP112 series has an address pin that allows addressing up to four devices on a single
bus. Table 2 describes the logic levels for correctly connecting up to four devices.


Table 2: Address Pin and Slave Address

|Two-Wire Address|ADD0 Pin Connection|
|---|---|
|1001000<br>1001001<br>1001010<br>1001011|Ground<br>V+<br>SDA<br>SCL|



8.3.6 Read and Write Operations


Access to specific registers on the KTP112 series is accomplished by writing the pointer
register to the appropriate value. The pointer register value is transmitted as the first byte
after the slave address byte with the _R_ / _W_ bit low. Each write operation to the KTP112
series requires a pointer register value (see Figure 8).


When reading from the KTP112 series, the last value stored in the pointer register by a
write operation determines which register is read during a read operation. To change the
register pointer for a read operation, the pointer register must be written to a new value.
This operation is accomplished by issuing a slave address byte with the _R_ / _W_ bit low, followed by a pointer register byte. No additional data is required. The master can then generate a start condition and send the slave address byte with the _R_ / _W_ bit high to initiate
the read command. See Figure 8 for more details on this sequence. If repeated reads from
the same register are required, the pointer register value does not need to be sent continuously because the KTP112 series retains the pointer register value until the next write
operation changes it.


Register bytes are sent MSB first, followed by LSB.


13 of 24


KTP112 Series


8.3.7 Slave Mode Operations


The KTP112 series can operate as a slave receiver or slave transmitter. As a slave device,
the KTP112 series never drives the SCL line.


Slave Receiver Mode The first byte transmitted by the master is the slave address with
the _R_ / _W_ bit low. The KTP112 series acknowledges receiving a valid address. The next byte
transmitted by the master is the pointer register. The KTP112 series acknowledges receiving the pointer register byte. The next byte or bytes are written to the register addressed
by the pointer register. The KTP112 series acknowledges receiving each data byte. The
master terminates data transfer by generating a start or stop condition.


Slave Transmitter Mode The first byte transmitted by the master is the slave address
with the _R_ / _W_ bit high. The slave address is received, and a valid address is acknowledged.
The next byte transmitted by the slave is the most significant byte of the register indicated
by the pointer register. The master acknowledges receiving the data byte. The next byte
transmitted by the slave is the least significant byte. The master acknowledges receiving
the data byte. The master can terminate data transfer by generating a start or stop condition or by not acknowledging the received data byte.


8.3.8 SMBus Alert Function


The KTP112 series supports the SMBus alert function. When the KTP112 series is in interrupt mode (TM=1), the alert pin can be connected as an SMBus alert signal. When the
master senses an alert condition on the alert line, the master sends an SMBus alert command (00011001) to the bus. If the alert pin is active, the device acknowledges the SMBus
alert command and responds by returning the slave address on the SDA line. The eighth
bit (LSB) of the slave address byte indicates whether the alert condition was caused by a
temperature exceeding _T_ _HIGH_ or falling below _T_ _LOW_ . If the temperature is greater than
_T_ _HIGH_, the LSB is high; if the temperature is less than _T_ _LOW_, the LSB is low. For more
details on this sequence, see Figure 10.


If multiple devices on the bus respond to the SMBus alert command, arbitration of the
slave address portion of the SMBus alert command determines which device clears its
alert status. The device with the lowest two-wire address wins the arbitration. If the KTP112
series wins the arbitration, the alert pin becomes inactive; if the KTP112 series loses the arbitration, the alert pin remains active.


8.3.9 General Call Response


The KTP112 series responds to a two-wire general call address (0000000) if the eighth
bit is 0. The device acknowledges the general call address and responds to the command
in the second byte. If the second byte is 00000110, the KTP112 series resets its internal
registers to the power-on initial values. The KTP112 series does not support the general
address acquire command.


8.3.10 High-Speed (HS) Mode


To enable two-wire bus operation above 400 _kHz_, the master device must issue an Hsmode master code (0000 1xxx) as the first byte after a start condition to switch the bus to
high-speed operation. The KTP112 series does not acknowledge this byte but switches the
input and output filter on the SDA and SCL pins to operate in Hs-mode, allowing transfers
up to 2 _._ 85 _MHz_ . After the Hs-mode master code is issued, the master transmits a twowire slave address to initiate a data transfer operation. The bus continues to operate in
Hs-mode until a stop condition is generated on the bus. After a stop condition is received,
the KTP112 series switches the input and output filters back to fast-mode operation.


8.3.11 Timeout Function


If the SCL pin is held low for 30 _ms_ (typical) between a start and stop condition, the KTP112
series resets the serial interface. If the SCL pin is held low and waits for a start condition
from the master controller, the KTP112 series releases the SDA line. To avoid activating the
timeout function, keep the SCL working frequency at least 1 _kHz_ .


14 of 24


KTP112 Series


8.3.12 Timing Diagrams


The KTP112 series is compatible with SMBus and I [2] C interfaces. Figures 7 to Figure 10
describe various operations on the KTP112 series. Parameters for Figure 7 are defined in
the Timing Requirements section. The bus definitions are as follows:

### • [Bus Idle][: Both SDA and SCL lines remain high.] • [Start Data Transfer][: A change in the state of the SDA line, from high to low, while]

the SCL line is high, defines a start condition. Each data transfer is initiated with a
start condition.

### • [Stop Data Transfer][: A change in the state of the SDA line, from low to high, while]

the SCL line is high, defines a stop condition. Each data transfer is terminated with
a repeated start or stop condition.
### • [Data Transfer][: The number of data bytes transferred between a start and stop con-]

dition is not limited and is determined by the master device. The KTP112 series can
also be used for single-byte updates. To update only the MS byte, terminate the
communication by issuing a start or stop condition on the bus.
### • [Acknowledge][: Each receiving device, when addressed, is obliged to generate an]

acknowledge bit. The master device must generate an extra clock pulse which is associated with this acknowledge bit. The device that acknowledges must pull down
the SDA line during the acknowledge clock pulse in such a way that the SDA line
is stable low during the high period of the acknowledge-related clock pulse. Setup
and hold times must be taken into account. On a master receive, the termination
of the data transfer can be signaled by a not-acknowledge (1) for the last byte received.


Figure 7: I [2] C Timing Diagram


Figure 8: Write Register Timing Diagram


A0 and A1 are determined by the ADD0 pin.


15 of 24


KTP112 Series


Figure 9: Read Register Timing Diagram


1) A0 and A1 are determined by the ADD0 pin. 2) The user should keep SDA high to terminate a single-byte read operation. 3) The user should keep SDA high to terminate a twobyte read operation.


Figure 10: SMBus ALERT Timing Diagram


A0 and A1 are determined by the ADD0 pin.


8.4 Device Functional Modes


8.4.1 Continuous Conversion Mode


The default mode of the KTP112 series is continuous conversion mode. In continuous
mode, the ADC performs continuous temperature conversions and stores each result in
the temperature register, overwriting the previous result. The conversion rate bits, CR1
and CR0, configure the KTP112 series for conversion rates of 0 _._ 25 _Hz_, 1 _Hz_, 4 _Hz_, or 8 _Hz_ .
The typical conversion time for the KTP112 series is 124 _ms_ . To achieve different conversion
rates, the KTP112 series performs a conversion, powers down, and waits for the appropriate
delay set by CR1 and CR0. Table 3 lists the CR1 and CR0 settings.


Table 3: Conversion Rate Settings

|CR1|CR0|Conversion Rate|
|---|---|---|
|0<br>0<br>1<br>1|0<br>1<br>0<br>1|0_._25_Hz_<br>1_Hz_<br>4_Hz_ (default)<br>8_Hz_|



After power-up or a general reset, the KTP112 series begins conversions immediately, as


16 of 24


KTP112 Series


shown in Figure 11. The first result is available after 124 _ms_ (typical). The active standby

�
current during conversion is 13 _._ 7 _µA_ (typical at 27 _C_ ). The standby current during the delay

�
period is 3 _._ 9 _µA_ (typical at 27 _C_ ).


Figure 11: Conversion Start


Standby time is determined by CR1 and CR0.


The average power consumption of the device in continuous mode can be calculated using
Equation below:


Average Power Consumption = [Active Power] _[ ×]_ [ Active Conversion Time][ +][ Standb][y][ Power] _[ ×]_ [ Standb][y][ Time]

Conversion Time Period


8.4.2 One-Shot/Conversion Ready Mode (OS)


The KTP112 series features a one-shot temperature measurement mode. When the device
is in shutdown mode, writing a 1 to the OS bit initiates a single temperature conversion.
During conversion, the OS bit reads 0. After the single conversion is completed, the device
returns to shutdown mode. The OS bit reads 1 after conversion. This feature can be used
to reduce the KTP112 series power consumption when continuous temperature monitoring
is not required. Due to the short conversion time, the KTP112 series can achieve high conversion rates. A single conversion typically occurs in 124 _ms_, and a read can occur in less
than 20 _µs_ . Using one-shot mode, up to eight conversions per second can be achieved.


Figure 12: One-Shot Measurement Mode Timing Diagram


17 of 24


KTP112 Series


8.4.3 Thermostat Mode (TM)


The thermostat mode bit indicates whether the device operates in comparator mode
(TM=0) or interrupt mode (TM=1).


8.4.4 Comparator Mode (TM=0)


In comparator mode (TM=0), the alert pin is activated when the temperature equals or
exceeds the value in the _T_ _HIGH_ register and remains active until the temperature falls
below the value in the _T_ _LOW_ register. For more information on comparator mode, see the
upper and lower limit registers section.


8.4.5 Interrupt Mode (TM=1)


In interrupt mode (TM=1), the alert pin is active when the temperature exceeds the _T_ _HIGH_
register or falls below the _T_ _LOW_ register. The alert pin is cleared when the host controller
reads the temperature register. For more information on interrupt mode, see the upper and
lower limit registers section.


8.5 Configuration


8.5.1 Pointer Register


Figure 13 shows the internal register structure of the KTP112 series. The device uses an 8bit pointer register to address a given data register. The pointer register uses the two LSBs
to identify which data register must respond to a read or write command. The power-on
reset value of P1/P0 is ”00”. By default, the KTP112 series reads the temperature register

upon power-up.


Figure 13: Internal Register Structure


Table 4 lists the pointer addresses of the available registers in the KTP112 series. Table
5 lists the bits of the pointer register byte. Bits P2 to P7 must always be 0 in write commands.


18 of 24


KTP112 Series


Table 4: Pointer Addresses

|P1|P0|Register|
|---|---|---|
|0<br>0<br>1<br>1|0<br>1<br>0<br>1|Temperature Register (Read-only)<br>Configuration Register (Read/Write)<br>_TLOW_ Register (Read/Write)<br>_THIGH_ Register (Read/Write)|



Table 5: Pointer Register Byte

|P7|P6|P5|P4|P3|P2|P1|P0|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|Register Bits|Register Bits|



8.5.2 Temperature Register


The temperature register in the KTP112 series is configured as a 16-bit read-only register
that must be read as two bytes to obtain data, as shown in Tables 6 and Figure 7. The 16bit data with sign bits is used to indicate the temperature.


Table 6: High Byte of the Temperature Register

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|T15|T14|T13|T12|T11|T10|T9|T8|



Table 7: Low Byte of the Temperature Register

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|2|T7|T6|T5|T4|T3|T2|T1|T0|



8.5.3 Configuration Register


The configuration register is a 16-bit read/write register used to store bits controlling the
operating modes of the temperature sensor. Read/write operations are performed MSB
first. Table 8 lists the format of the configuration register and the power-on default values.


Table 8: Configuration and Power-On Default Values

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|OS<br>0|R1<br>1|R0<br>1|F1<br>0|F0<br>0|POL<br>0|TM<br>0|SD<br>0|
|2|CR1<br>1|CR0<br>0|AL<br>1|EM<br>0|0<br>0|0<br>0|0<br>0|0<br>0|



Shutdown Mode (SD) Shutdown mode saves maximum power by turning off all device
circuitry except for the serial interface, reducing the current consumption to typically less
than 0 _._ 25 _µA_ . When the SD bit=1, shutdown mode is enabled; the device shuts down once
the current conversion is completed. When the SD bit=0, the device remains in continuous
conversion state.


Thermostat Mode (TM) The thermostat mode bit indicates whether the device operates
in comparator mode (TM=0) or interrupt mode (TM=1).


19 of 24


KTP112 Series


Polarity (POL) The polarity bit allows the user to adjust the polarity of the ALERT pin
output. If the POL bit is set to 0, the ALERT pin is active low. When the POL bit is set to 1,
the ALERT pin is active high and the state of the ALERT pin is inverted.


Figure 14: Output Transfer Function


Fault Queue (F1/F0) A fault condition exists when the measured temperature exceeds
the user-defined limits set in the _T_ _HIGH_ and _T_ _LOW_ registers. Additionally, the fault queue
can be used to program the number of fault conditions required to generate an alert. The
fault queue is provided to prevent false alerts due to environmental noise. The fault queue
requires consecutive fault measurements to trigger an alert. Table 9 lists the possible settings for the number of fault measurements that can trigger an alert condition in the device.


Table 9: KTP112 Series Fault Settings

|F1|F0|Number of Consecutive Faults|
|---|---|---|
|0<br>0<br>1<br>1|0<br>1<br>0<br>1|1<br>2<br>4<br>6|



One-Shot Mode (OS) When the device is in shutdown mode, writing a 1 to the OS bit
starts a single temperature conversion. During conversion, the OS bit reads 0. After the
single conversion is completed, the device returns to shutdown mode. For more information on one-shot conversion mode, see the One-Shot/Conversion Ready Mode (OS)
section.


Alert (AL) The AL bit is a read-only function. Reading the AL bit provides information on
the status of comparator mode. The state of the POL bit inverts the polarity of the data
returned from the AL bit. When POL bit equals 0, the AL bit reads 1 until the temperature
equals or exceeds _T_ _HIGH_ for the programmed number of consecutive faults, causing the
AL bit to read 0. The AL bit continues to read 0 until the temperature falls below _T_ _LOW_ for
the programmed number of consecutive faults, then reads 1 again. The state of the TM bit


20 of 24


KTP112 Series


does not affect the state of the AL bit.


8.5.4 Upper and Lower Limit Registers


Temperature limits are stored in the _T_ _HIGH_ and _T_ _LOW_ registers in the same format as the
temperature result and compared to the temperature result at each conversion. The result
of the comparison drives the behavior of the ALERT pin, which operates as a comparator
output or interrupt, set by the TM bit in the configuration register.


In comparator mode (TM=0), the ALERT pin becomes active when the temperature equals
or exceeds the value in the _T_ _HIGH_ register and remains active until the temperature falls
below the value in the _T_ _LOW_ register for the programmed number of consecutive faults.


In interrupt mode (TM=1), the ALERT pin is active when the temperature equals or exceeds
the value in the _T_ _HIGH_ register or falls below the value in the _T_ _LOW_ register, seen in the
Table 8. The ALERT pin is cleared when any register is read, or the device successfully
responds to the SMBus alert response address. If the device is in shutdown mode, the
ALERT pin is also cleared. The ALERT pin will be reactivated only if the temperature exceeds _T_ _HIGH_ or falls below _T_ _LOW_ for the programmed number of consecutive faults.
This operation will also clear the status of the internal registers in the device, returning the
device to comparator mode (TM=0). Both operation modes are shown in Figure 14. Tables
10 and Table 11 list the formats of the _T_ _HIGH_ and _T_ _LOW_ registers.


The power-on reset values of _T_ _HIGH_ and _T_ _LOW_ are:

### • [T] HIGH [=][ 80] [�] [C] • [T] LOW [=][ 75] [�] [C]


The data format for _T_ _HIGH_ and _T_ _LOW_ is the same as the temperature register.


Table 10: High Byte and Low Byte of the _T_ _HIGH_ Register

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|H15|H14|H13|H12|H11|H10|H9|H8|
|2|H7|H6|H5|H4|H3|H2|H1|H0|



Table 11: High Byte and Low Byte of the _T_ _LOW_ Register

|BYTE|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|---|
|1|L15|L14|L13|L12|L11|L10|L9|L8|
|2|L7|L6|L5|L4|L3|L2|L1|L0|


## 9 Applications and Implementation


9.1 Application Information


The KTP112 series is used to measure the PCB temperature at the device installation site.
Programmable address options allow monitoring up to four locations on a single serial bus.


21 of 24


KTP112 Series


9.2 Typical Application Schematic


Figure 15: Typical Connection


The SCL, SDA, and Alert pins require pull-up resistors.


9.3 Design Requirements


The KTP112 series requires pull-up resistors on the SCL, SDA, and ALERT pins. The recommended value for the pull-up resistors is 5 _k_ Ω. In some applications, the pull-up resistors
can be lower or higher than 5 _k_ Ω, but should not be less than 500Ω or exceed 10 _mA_ current on any of these pins. A 0 _._ 1 _µF_ bypass capacitor is recommended on the power supply,
as shown in Figure 15. The SCL and SDA lines can be pulled up to a power supply equal
to or higher than V+. To configure one of four different addresses on the bus, connect the
ADD0 pin to GND, V+, SDA, or SCL.


9.4 Detailed Design Procedure


Place the device near the heat source that needs to be monitored to achieve good thermal coupling. This positioning ensures that temperature changes are captured within the
shortest time interval. For applications requiring accurate air or surface temperature measurements, take care to isolate the package and leads from ambient air temperature. A
thermally conductive adhesive helps achieve accurate surface temperature measurements.


The KTP112 series is a very low power device and generates very low noise on the power
supply bus. Applying an RC filter to the V+ pin of the KTP112 series can further reduce any
noise the device may propagate to other components. In Figure 16, _R_ _F_ must be less than
5 _k_ Ω and _C_ _F_ must be greater than 10 _nF_ .


22 of 24


KTP112 Series


Figure 16: Noise Reduction Techniques


9.5 Application Curves


Figure 17 shows the step response of the KTP112 series immersed in a 100 � _C_ oil bath at
room temperature (26 � _C_ ). The time constant, or the time to reach 63% of the input step,
is 3 _._ 1 _s_ . The result of the time constant depends on the PCB on which the KTP112 series is
mounted. In this test, the KTP112 series is soldered onto a two-layer PCB measuring 1 _._ 5
inches _×_ 1 _._ 5 inches.


Figure 17: Temperature Step Response

## 10 Power Supply Recommendations


The KTP112 series has a power supply range of 1 _._ 8 _V_ to 5 _._ 5 _V_ . The device is optimized to
operate at 3 _._ 3 _V_ but can accurately measure temperature across the entire power supply
range. A power supply bypass capacitor is required for proper operation. Place this capacitor as close as possible to the power and ground pins of the device. The typical value of
this power supply bypass capacitor is 0 _._ 1 _µF_ . Applications with noisy or high impedance
power supplies may require additional decoupling capacitors to suppress power supply
noise.


23 of 24


KTP112 Series

## 11 Ordering Information

|Part number|Package Type|MSL|Peak Temp (°C)|Operating Temp (°C)|
|---|---|---|---|---|
|KTP112-DZ6|DFN2×2-6L|Level-3|260|_−_40 to 125|


## 12 Package Information


Figure 18: DFN2×2-6L Package Dimensions


24 of 24




</details>

---

## 相关资源

### PDF文档
- [📋 KTP112_CN.pdf](/pdfs/KTP112_CN.pdf)
- [📋 KTP112_Datasheet_EN.pdf](/pdfs/KTP112_Datasheet_EN.pdf)

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

- [KTH462N 增强版](./KTH462N.md) - 同系列产品
- [KTAX333 增强版](./KTAX333.md) - 同系列产品
### 3D霍尔传感器

- [KTH31xx 增强版](./KTH31xx.md) - 推荐3D霍尔传感器
### 磁编码器

- [KTH7801 增强版](./KTH7801.md) - 推荐磁编码器
### 霍尔开关

- [KTH1201 增强版](./KTH1201.md) - 推荐霍尔开关

---
