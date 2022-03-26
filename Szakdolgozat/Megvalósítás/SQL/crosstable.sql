create table names_to_correct (id int, uid int, Names varchar)

select * from fasz where name like '%mane'

select 
	ntc.uid as ntcuid, ntc.names as ntcnames,ps.uid as psuid, ps.name as psname into cross_table
from 
	names_to_correct ntc
inner join
	fasz ps 
		on ps.name like ntc.names
		
		select * from cross_table
		
	CREATE UNIQUE INDEX ntc_names ON names_to_correct (names);
	CREATE UNIQUE INDEX player_stg_name ON player_stg (name);
	CREATE UNIQUE INDEX fasz_name ON fasz (name);
	
	
	select * into fasz from fasz_temp where uid in (
	
	select min(uid) from fasz group by name having count(*) = 1 )
	