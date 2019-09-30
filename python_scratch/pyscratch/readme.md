# pyscratch
参考B站up主：[少儿编程](https://space.bilibili.com/342243515?spm_id_from=333.788.b_765f7570696e666f.2)
>https://www.bilibili.com/video/av52534374

### 配置:
`pip install pyscratch`

# 引用
## What is pyscratch (pyscratch 是什么)
Pyscratch is a python lib for programming education for children, provide api like mit scratch.     
Pyscratch 是专为少儿编程教育开发的python库，让孩子学习python更容易，更有趣，接口和 Scratch是一样的，可以做出scratch一样好玩的游戏。    
tutorial（教程）: https://www.bilibili.com/video/av53134211
       
## How to use pyscratch (怎样使用Pyscratch)
pip install pyscratch
         
## Pyscratch API （接口使用手册）

---
## 运动  ##

---
#### move(steps)  
移动指定距离  
参数  
steps 


#### turn_right(degrees)   
右转指定角度  
参数：
degrees 度  

 
#### turn_left(degrees)     
左转指定角度  
参数：
degrees 度  


#### go_to_random_position()  
移动到随机位置  


#### go_to_mouse_pointer()  
移动到鼠标位置  


#### go_to(x,y)  
移动到坐标
参数  
x x坐标  
y y坐标  


#### glide_to_random_position(secs)
在指定时间内，滑动到随机位置
参数：
secs 时间，单位秒


#### glide_to_mouse_pointer(secs)  
在指定时间内，滑动到鼠标位置  
参数：
secs 时间，单位秒  


#### glide_to(secs,x,y)  
在指定时间内，滑动到坐标位置  
参数： 
secs 时间，单位秒  
x x坐标  
y y坐标  


#### point(direction)  
朝向某个方向  
参数：  
direction 单位度  


#### point_towards_mouse_pointer()

#### change_x_by(x)

#### set_x_to(x)

#### change_y_by(y)

#### set_y_to(y)

#### bounce_if_on_edge()

#### set_rotation_style(style)

#### x

#### y

#### direction  





---


## 外观

#### say_for_seconds(text, secs)

#### say(text)

#### think_for_seconds
未实现

#### think_for_seconds
未实现

#### switch_costume_to(costume_name)

造型切换为
参数些精灵文件夹内的图片文件名，不用写图片扩展名


#### next_costume()
下一个场景

#### switch_backdrop_to()

#### next_backdrop(backdrop_name)
未实现

#### change_size_by(num)
改变精灵大小

#### set_size_to(num)
设置精灵大小

#### change_effect_by()
未实现

effect 枚举

#### set_effect_to()
未实现

effect 枚举

#### clear_graphic_effects()
未实现

#### show()
显示精灵

#### hide()
隐藏精灵

#### goto_front_layer()
转到上面图层
未实现

#### goto_back_layer()
转到下面图层
未实现

#### go_forward_layer(num)
未实现

#### go_backward_layer(num)
未实现

#### costume{}
字典类型变量，可以通过[数组] 或 [名称] 访问


#### backdrop{}
字典类型变量，可以通过[数组] 或 [名称] 访问


#### size 精灵的size

## 声音

#### play_sound_until_done(sound)
未实现

#### play_sound(sound_name)
播放声音
参数些声音文件名, 带扩展名

#### stop_all_sounds()
未实现

#### change_effect_by()
(和外观都有类似方法)

#### set_effect_to()
未实现

参数：
声调 pitch
左右平衡 pan_left_right


#### clear_sound_effects()
清除所有音效

#### change_volumn_by()
将音量增加

#### set_volumn_to()
将音量设为 %

#### volumn



## 事件

#### when_start(func)
当程序开始运行时，触发func
func是一个函数的函数名

#### when_key_pressd(key_index,func)
当某键盘按键被按下时，触发func
func是一个函数的函数名
所有的键盘事件都是K_ 开头
未实现

#### when_clicked(func)
当某键盘按键被按下时，触发func
func是一个函数的函数名


#### when_backdrop_switch_to()


#### when_loudness_greater_than()


#### when_timer_greater_than()


#### when_receive(event_name, func)
当接受到某时间，执行func


#### broadcast(message)
广播事件
未实现

#### broadcast_and_wait(message)



## 控制


#### wait(seconds)
等待 seconds 秒

#### wait_util(message)


#### stop_all()


#### stop_this()


#### stop_other()


#### when_start_as_clone()


#### clone(sprite)


#### delete_this_clone()



## 侦测

#### touching_mouse_pointer()


#### touching_edge()


#### touching_color(color)


#### touching_color(color1,color2)


#### distance_to_mouse_pointer()


#### ask_and_wait(question)


#### key_pressed(key)
侦测键盘按键被按下事件，所有事件都已K_开头

#### mouse_down()  


#### mouse_x  


#### mouse_y  


#### set_drag_mode(mode)
参数：
mode True 或 False  


#### loudness


#### timer


#### reset_timer()  


#### backdrop


#### backdrop_name


#### volume


#### year


#### month


#### date


#### day_of_week


#### hour


#### minute


#### second

