CREATE TABLE `物料表` (
  `物料号` int NOT NULL,
  `名称` varchar(45) DEFAULT NULL,
  `单位` varchar(45) DEFAULT NULL,
  `调配方式` varchar(45) DEFAULT NULL,
  `损耗率` double DEFAULT NULL,
  `作业提前期` int DEFAULT NULL,
  PRIMARY KEY (`物料号`)
);

CREATE TABLE `库存表` (
  `物料号` int NOT NULL,
  `物料名称` varchar(45) DEFAULT NULL,
  `工序库存` int DEFAULT NULL,
  `资材库存` int DEFAULT NULL,
  PRIMARY KEY (`物料号`),
  CONSTRAINT `id` FOREIGN KEY (`物料号`) REFERENCES `物料表` (`物料号`)
);

CREATE TABLE `调配构成表` (
  `调配基准编号` varchar(45) DEFAULT NULL,
  `调配区代码` varchar(45) DEFAULT NULL,
  `父物料号` int NOT NULL,
  `父物料名称` varchar(45) DEFAULT NULL,
  `子物料号` int NOT NULL,
  `子物料名称` varchar(45) DEFAULT NULL,
  `构成数` int DEFAULT NULL,
  `配料提前期` int DEFAULT NULL,
  `供应商提前期` int DEFAULT NULL,
  PRIMARY KEY (`父物料号`,`子物料号`),
  KEY `son_idx` (`子物料号`),
  CONSTRAINT `father` FOREIGN KEY (`父物料号`) REFERENCES `物料表` (`物料号`),
  CONSTRAINT `son` FOREIGN KEY (`子物料号`) REFERENCES `物料表` (`物料号`)
);

CREATE TABLE `mps` (
  `id` int NOT NULL AUTO_INCREMENT,
  `产品名称` varchar(45) DEFAULT NULL,
  `数量` int DEFAULT NULL,
  `完工日期` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `bs` (
  `id` int NOT NULL,
  `资产类说明` varchar(45) DEFAULT NULL,
  `资产类方向` varchar(45) DEFAULT NULL,
  `资产类汇总序号` int DEFAULT NULL,
  `变量名` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `query_bs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `变量名` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `erp`.`物料表`
(`物料号`,
`名称`,
`单位`,
`调配方式`,
`损耗率`,
`作业提前期`)
VALUES
(20000,"眼镜","副","生产",0.0,1),
(20100,"镜框","副","生产",0.0,2),
(20109,"螺钉","个","采购",0.1,0),
(20110,"镜架","个","采购",0.0,0),
(20120,"镜腿","个","采购",0.0,0),
(20130,"鼻托","个","采购",0.0,0),
(20300,"镜片","片","采购",0.0,0);

INSERT INTO `erp`.`库存表`
(`物料号`,
`物料名称`,
`工序库存`,
`资材库存`)
VALUES
(20000,"眼镜",0,0),
(20100,"镜框",0,0),
(20109,"螺钉",10,50),
(20110,"镜架",0,0),
(20120,"镜腿",10,20),
(20130,"鼻托",0,0),
(20300,"镜片",0,0);

INSERT INTO `erp`.`调配构成表`
(`调配基准编号`,
`调配区代码`,
`父物料号`,
`父物料名称`,
`子物料号`,
`子物料名称`,
`构成数`,
`配料提前期`,
`供应商提前期`)
VALUES
("000001","L001",20000,"眼镜",20100,"镜框",1,0,0),
("000001","L001",20000,"眼镜",20109,"螺钉",2,1,10),
("000001","L001",20000,"眼镜",20300,"镜片",2,1,20),
("000001","L003",20100,"镜框",20109,"螺钉",4,1,10),
("000001","L003",20100,"镜框",20110,"镜架",1,1,20),
("000001","L003",20100,"镜框",20120,"镜腿",2,1,10),
("000001","L003",20100,"镜框",20130,"鼻托",2,1,18);

INSERT INTO `erp`.`bs`
(`id`,
`资产类说明`)
VALUES
('1', '流动资产：');

INSERT INTO `erp`.`bs`
(`id`,
`资产类说明`,
`资产类方向`,
`资产类汇总序号`,
`变量名`)
VALUES
('2', '货币资金', '+', '16', 'a1'),
('3', '短期投资', '+', '16', 'a3'),
('4', '应收票据', '+', '16', 'a5'),
('5', '应收账款', '+', '7', 'a7'),
('6', '减：坏账准备', '+', '7', 'a9'),
('7', '应收账款净额', '+', '16', 'b1'),
('8', '预付账款', '+', '16', 'a12'),
('9', '应收补贴款', '+', '16', 'a14'),
('10', '其他应收款', '+', '16', 'a16'),
('11', '存货', '+', '16', 'a18'),
('12', '待摊费用', '+', '16', 'a20'),
('13', '待处理流动资产净损失', '+', '16', 'a22'),
('14', '一年内到期的长期债券投资', '+', '16', 'a24'),
('15', '其他流动资产', '+', '16', 'a26'),
('16', '流动资产合计', '+', '35', 'b3');