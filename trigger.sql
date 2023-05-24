use crowdvis;
CREATE TRIGGER log_staff_operation 
AFTER UPDATE ON app_staff 
FOR EACH row
begin
   INSERT INTO app_trace_tabel_staff(user_id,`time`,staff_id,join_id,name,username,password,scenic_plot_id) 
   values(old.staff_id,NOW(),new.staff_id,new.join_id,new.name,new.username,new.`password`,new.scenic_plot_id);
end;


create trigger anti_abnormal_data
before insert on app_staff
for each row 
begin
	if new.staff_id<=0 then 
	insert into app_error_log values (id,"insert data error!",NOW());
	end if;
end;


