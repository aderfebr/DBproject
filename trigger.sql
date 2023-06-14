use project;

create table trace_update_staff(
 	id int NOT NULL AUTO_INCREMENT,
 	user_info varchar(50),
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
   INSERT INTO trace_update_staff(user_info,update_time,update_staff_id,update_join_id,update_name,update_username,update_password,update_plot_id) 
   values(user(),NOW(),new.staff_id,new.join_id,new.name,new.username,new.password,new.scenic_plot_id);
end;

CREATE TRIGGER staff_job 
AFTER insert ON app_staff 
FOR EACH row
begin
	begin
		if new.staff_id like '1%' then
		insert into app_security_personnel(staff_id_id)
		values
		(new.staff_id);
		else
		insert into app_maintain_personnel(staff_id_id)
		values
		(new.staff_id);
		end if;
	end;
end;

drop trigger staff_job




insert into 
app_scenic_plot 
values
(1,'景点1','上海市'),
(2,'景点2','上海市'),
(3,'景点3','上海市')

insert into 
app_area 
values
('1001a',"游乐设施",'区域1','1'),
('1002a',"观光设施",'区域2','1'),
('1003a',"休闲设施",'区域3','2'),
('1004a',"观光设施",'区域4','3'),
('1005a',"普通设施",'区域5','2')

insert into
app_device(device_id,device_name,manufacturer,production_date,func,area_id_id)
values
('1001d','摄像头1','上海市XXX公司','2020-5-20','监控人流量','1001a'),
('1002d','报警器1','上海市YYY公司','2019-10-5','人流量超限时发出警报','1001a'),
('1003d','扩音器1','上海市ZZZ公司','2020-1-20','警报通知','1002a'),
('1004d','摄像头2','上海市XXX公司','2020-5-21','监控人流量','1002a'),
('1005d','报警器2','上海市YYY公司','2019-9-6','人流量超限时发出警报','1002a'),
('1006d','扩音器2','上海市ZZZ公司','2020-2-10','警报通知','1002a'),
('1007d','摄像头3','上海市XXX公司','2020-5-21','监控人流量','1003a'),
('1008d','报警器3','上海市YYY公司','2019-9-6','人流量超限时发出警报','1003a'),
('1009d','扩音器3','上海市ZZZ公司','2020-2-10','警报通知','1003a'),
('1010d','摄像头4','上海市XXX公司','2020-7-23','监控人流量','1004a'),
('1011d','报警器4','上海市YYY公司','2020-3-6','人流量超限时发出警报','1004a'),
('1012d','扩音器4','上海市ZZZ公司','2020-5-28','警报通知','1005a'),
('1013d','摄像头5','上海市XXX公司','2020-7-23','监控人流量','1005a'),
('1014d','报警器5','上海市YYY公司','2020-3-6','人流量超限时发出警报','1005a'),
('1015d','扩音器5','上海市ZZZ公司','2020-5-28','警报通知','1002a');

insert into
app_warning(warn_time,warn_type,warn_area,warn_description,info,device_id_id)
values
('2023-6-13','进人流量超限','区域1','无描述','未处理','1001d'),
('2023-6-11','出现摔倒行为','区域2','无描述','未处理','1002d'),
('2023-6-11','总流量超限','区域3','无描述','未处理','1005d'),
('2023-6-10','出流量超限','区域1','无描述','未处理','1010d'),
('2023-6-9','出流量超限','区域3','无描述','未处理','1005d'),
('2023-6-9','滞留流量超限','区域5','无描述','未处理','1002d'),
('2023-6-8','出现打架行为','区域4','无描述','未处理','1005d');


insert into 
app_security_report(sreport_date,sreport,area_id_id,staff_id_id)
values
('2023-6-10','无异常情况','1002a','10001'),
('2023-6-11','总人流量超限，实施人流疏导工作','1002a','10001'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1003a','10002'),
('2023-6-10','无异常情况','1004a','10001'),
('2023-6-11','总人流量超限，实施人流疏导工作','1004a','10002'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1003a','10003'),
('2023-6-10','无异常情况','1002a','10001'),
('2023-6-11','总人流量超限，实施人流疏导工作','1001a','10002'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1001a','10004'),
('2023-6-10','无异常情况','1002a','10006'),
('2023-6-11','总人流量超限，实施人流疏导工作','1003a','10005'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1004a','10007'),
('2023-6-10','无异常情况','1002a','10008'),
('2023-6-11','总人流量超限，实施人流疏导工作','1001a','10009'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1003a','10009'),
('2023-6-10','无异常情况','1002a','10008'),
('2023-6-11','总人流量超限，实施人流疏导工作','1002a','10007'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1003a','10003'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1004a','10011'),
('2023-6-10','无异常情况','1002a','10010'),
('2023-6-11','总人流量超限，实施人流疏导工作','1002a','10006'),
('2023-6-12','有紧急情况导致人流量滞留，已进行疏散','1003a','10006')


insert into 
app_maintain_report(mreport_date,mreport,device_id_id,staff_id_id)
values
('2023-6-1','设备无异常情况','1002d','20001'),
('2023-6-2','设备无异常情况','1001d','20001'),
('2023-6-3','摄像头故障，已解决','1004d','20002'),
('2023-6-3','报警器故障，已解决','1008d','20003'),
('2023-6-4','设备无异常情况','1010d','20010'),
('2023-6-5','设备无异常情况','1011d','20005'),
('2023-6-5','设备无异常情况','1008d','20004'),
('2023-6-6','设备无异常情况','1002d','20011'),
('2023-6-7','设备无异常情况','1004d','20002'),
('2023-6-8','设备无异常情况','1007d','20003'),
('2023-6-9','设备无异常情况','1005d','20008'),
('2023-6-10','设备无异常情况','1006d','20009')

select staff_id,join_id,name,username,password,scenic_plot_id,grade
from app_staff a,app_security_personnel b
where a.staff_id = b.staff_id_id 


select sreport_id,sreport_date,staff_id_id,id,sreport,area_id_id,sreport_id_id 
from app_security_report a,app_security_report_area b 
where a.sreport_id = b.sreport_id_id



create view security_view
as
select 
staff_id,join_id,name
from
app_staff,app_security_personnel
where 
app_staff.staff_id=app_security_personnel.staff_id_id;

create view maintain_view
as
select 
staff_id,join_id,name
from
app_staff,app_maintain_personnel 
where 
app_staff.staff_id=app_maintain_personnel.staff_id_id;

drop view security_view;
drop view maintain_view;




