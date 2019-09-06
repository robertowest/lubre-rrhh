-- NUEVO
CREATE OR REPLACE VIEW activo_mantenimiento_view
AS
   select a.responsable_id,
          a.id as activo_id, a.tipo, a.descripcion as activo,
          m.id as mantenimiento_id, m.descripcion as mantenimiento, m.estado, m.proximo, m.fecha_inicial, m.fecha_final, m.archivo
     from rrhh_activo a
left join rrhh_mantenimiento m on m.activo_id = a.id
    where a.active = 1 and ifnull(m.active, 1) = 1
 order by a.tipo, a.descripcion



-- OBSOLETO
CREATE OR REPLACE VIEW activo_mantenimiento_view
AS
-- documentos y mantenimientos
select
    Null AS `act_id`,
    Null AS `tipo`,
    Null AS `activo`,
    `d`.`id` AS `doc_id`,
    `d`.`descripcion` AS `documentacion`,
    `d`.`fecha_inicial` AS `valido_desde`,
    `d`.`fecha_final` AS `valido_hasta`,
    `ma`.`id` AS `mant_id`,
    `ma`.`descripcion` AS `mantenimiento`,
    `ma`.`estado` AS `estado`,
    `ma`.`proximo` AS `proximo`,
    `d`.`responsable_id` AS `responsable_id`
from
    (`lubresrl`.`rrhh_documentacion` `d`
left join `lubresrl`.`rrhh_mantenimiento` `ma` on (`ma`.`object_id` = `d`.`id` and `ma`.`content_type_id` = 30))
where `d`.`active` = 1
UNION ALL
-- activos y mantenimientos
select
    `a`.`id` AS `act_id`,
    `a`.`tipo` AS `tipo`,
    `a`.`identificacion` AS `activo`,
    Null AS `doc_id`,
    Null AS `documentacion`,
    Null AS `valido_desde`,
    Null AS `valido_hasta`,
    `ma`.`id` AS `mant_id`,
    `ma`.`descripcion` AS `mantenimiento`,
    `ma`.`estado` AS `estado`,
    `ma`.`proximo` AS `proximo`,
    `a`.`responsable_id` AS `responsable_id`
from
    (`lubresrl`.`rrhh_activo` `a`
left join `lubresrl`.`rrhh_mantenimiento` `ma` on (`ma`.`object_id` = `a`.`id` and `ma`.`content_type_id` = 32))
where
    `a`.`active` = 1
    and `ma`.`id` is not Null
UNION ALL
-- activos, documentos y mantenimientos
select
    `a`.`id` AS `act_id`,
    `a`.`tipo` AS `tipo`,
    `a`.`identificacion` AS `activo`,
    `d`.`id` AS `id`,
    `d`.`descripcion` AS `documentacion`,
    `d`.`fecha_inicial` AS `valido_desde`,
    `d`.`fecha_final` AS `valido_hasta`,
    `md`.`id` AS `id`,
    `md`.`descripcion` AS `mantenimiento`,
    `md`.`estado` AS `estado`,
    `md`.`proximo` AS `proximo`,
    `a`.`responsable_id` AS `responsable_id`
from
    ((`lubresrl`.`rrhh_activo` `a`
join `lubresrl`.`rrhh_documentacion` `d` on
    (`d`.`activo_id` = `a`.`id`))
left join `lubresrl`.`rrhh_mantenimiento` `md` on
    (`md`.`object_id` = `d`.`id`
    and `md`.`content_type_id` = 30))
where
    `a`.`active` = 1
    and (`d`.`id` is not Null or `md`.`id` is not Null)
order by tipo, activo, documentacion, mantenimiento
