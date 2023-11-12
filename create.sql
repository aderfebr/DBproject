create table items(
    item_id int primary key ,
    item_name varchar(50),
    price double,
    img_url varchar(50),
    info varchar(100),
    type int,
    type_name varchar(50),
    score int
);
create table orders(
    id int primary key auto_increment,
    user_id int,
    item_id int
);
insert into items
values
(1001,'AMD Ryzen ThreadRipper Pro 5995WX',48969.0,'','台式机	7纳米 2.7GHz	4.5GHz	256MB 六十四核心',0,'CPU',95),
(1002,'Intel 酷睿i9 7960X',11899.0,'','台式机	14纳米	2.8GHz	4.2GHz	22MB	十六核心	三十二线程',0,'CPU',88),
(1003,'AMD Ryzen ThreadRipper 3990X',29999.0,'','台式机	7纳米	2.9GHz	4.3GHz	256MB	六十四核心	一百二十八线程',0,'CPU',92),
(1004,'Intel 酷睿i9 9980XE',8199.0,'','台式机	14纳米	3GHz	4.4GHz	25MB	十八核心	三十六线程',0,'CPU',86),
(1005,'Intel 酷睿 i9 13900K',5500.0,'','10纳米	3GHz	5.8GHz	36MB	二十四核心	三十二线程',0,'CPU',80),
(1006,'Intel 酷睿i7 10700KF',2199.0,'','14纳米	3.8GHz	5.1GHz	16MB	八核心	十六线程',0,'CPU',56),
(1007,'三星870 QVO',5899.0,'','消费类	2TB	8GB	150万小时	SATA3	560MB/s	530MB/s',1,'SSD',90),
(1008,'西部数据Gold',8299.0,'','企业级	3.84TB	4GB	200万小时	U.2	3100MB/s	1800MB/s',1,'SSD',84),
(1009,'希捷FireCuda',2899.0,'','消费类	2TB	2GB	180万小时	M.2 PCIe	5000MB/s	4400MB/s',1,'SSD',72),
(1010,'三星990 PRO NVMe M.2',1149.0,'','消费类	2TB	暂无数据	暂无数据	M.2 PCIe	7450MB/s	6900MB/s',1,'SSD',64),
(1011,'微星GeForce RTX 3090 AERO',19000.0,'','专业级	GeForce RTX 3090	24GB	1695MHz	19500MHz	384bit',2,'VGA',92),
(1012,'华硕ROG-STRIX-RTX3090-O24G-GUNDAM',16999.0,'','GeForce RTX 3090	24GB	1860-1890MHz	19500MHz	384bit',2,'VGA',90),
(1013,'七彩虹iGame GeForce RTX 4080',11499.0,'','发烧级	GeForce RTX 4080	24GB	2205-2640MHz	22400MHz	256bit',2,'VGA',82),
(1014,'蓝宝石Radeon RX 6800 XT 16G',8299.0,'','Radeon RX 6800 XT	16GB	2110-2360MHz	16000MHz	256bit',2,'VGA',77),
(1015,'金士顿骇客神条FURY 16GB DDR4',470.0,'','台式机	DDR4	3200MHz',3,'RAM',80),
(1016,'芝奇幻锋戟 32GB（2×16GB）DDR5 6000',978.0,'','台式机	DDR5	6000MHz',3,'RAM',95),
(1017,'阿斯加特弗雷 Freyr 32GB（2×16GB）',799.0,'','台式机	DDR5	5200MHz',3,'RAM',90),
(1018,'影驰HOF CLASSIC DDR5 7000 16G*2',1299.0,'','台式机	DDR5	7000MHz',3,'RAM',98),
(1019,'梵想S500 PRO',699.0,'','暂无数据	150万小时	M.2 PCIe	3500MB/s	3150MB/s',1,'SSD',50),
(1020,'铠侠EXCERIA PRO',699.0,'','消费类	1TB	1GB	150万小时	M.2 PCIe	7300MB/s	6400MB/s',1,'SSD',66),
(1021,'华硕ROG-STRIX-GeForce-RTX4070TI',7589.0,'','主流级	GeForce RTX 4070Ti	12GB	2610MHz	21000MHz	192bit',2,'VGA',74)
insert into orders
values
(1,1001,1001),
(2,1001,1002),
(3,1001,1003),
(4,1002,1003),
(5,1003,1001),
(6,1003,1002),
(7,1004,1002),
(8,1005,1001);