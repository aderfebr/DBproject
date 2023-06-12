use project;

create table trace_update_staff(
 	id int NOT NULL AUTO_INCREMENT,
    update_time varchar(50),
    update_staff_id varchar(50),
    update_join_id varchar(50),
    update_name varchar(50),
    update_username varchar(50),
    update_password varchar(50),
    update_plot_id varchar(50),
    PRIMARY KEY (id)
);



CREATE TRIGGER log_staff_operation 
AFTER UPDATE ON app_staff 
FOR EACH row
begin
   INSERT INTO trace_update_staff(update_time,update_staff_id,update_join_id,update_name,update_username,update_password,update_plot_id) 
   values(NOW(),new.staff_id,new.join_id,new.name,new.username,new.password,new.scenic_plot_id);
end;



insert into 
app_scenic_plot values
(1,'景点1','上海市'),
(2,'景点2','上海市'),
(3,'景点3','上海市')

insert into 
app_area 
values
(1,"游乐设施",'区域1','1'),
(2,"观光设施",'区域2','1'),
(3,"休闲设施",'区域3','2'),
(4,"观光设施",'区域4','3'),
(5,"普通设施",'区域5','2')

insert into
app_device(device_id,device_name,manufacturer,production_date,`function`,area_id_id)
values
(1,'摄像头1','上海市XXX公司','2020-5-20','监控人流量',1),
(2,'报警器1','上海市YYY公司','2019-10-5','人流量超限时发出警报',1),
(3,'扩音器1','上海市ZZZ公司','2020-1-20','警报通知',1),
(4,'摄像头2','上海市XXX公司','2020-5-21','监控人流量',2),
(5,'报警器2','上海市YYY公司','2019-9-6','人流量超限时发出警报',2),
(6,'扩音器2','上海市ZZZ公司','2020-2-10','警报通知',2),
(7,'摄像头3','上海市XXX公司','2020-5-21','监控人流量',3),
(8,'报警器3','上海市YYY公司','2019-9-6','人流量超限时发出警报',3),
(9,'扩音器3','上海市ZZZ公司','2020-2-10','警报通知',3),
(10,'摄像头4','上海市XXX公司','2020-7-23','监控人流量',4),
(11,'报警器4','上海市YYY公司','2020-3-6','人流量超限时发出警报',4),
(12,'扩音器4','上海市ZZZ公司','2020-5-28','警报通知',5),
(13,'摄像头5','上海市XXX公司','2020-7-23','监控人流量',5),
(14,'报警器5','上海市YYY公司','2020-3-6','人流量超限时发出警报',5),
(15,'扩音器5','上海市ZZZ公司','2020-5-28','警报通知',5)

