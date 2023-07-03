SELECT *

FROM orders AS o

LEFT JOIN items AS i
ON o.item_id = i.id_item

WHERE i.item_name = 'Lamp';
