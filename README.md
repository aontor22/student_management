# student_management
Odoo 18 module for managing students and courses with a many-to-many enrollment.

## Install and run
1. Create a `custom_addons` folder inside the Odoo 18 server folder and put `student_management` inside it.
2. Edit `odoo.conf` and set:
   - `addons_path = E:/Odoo 18/server/custom_addons,E:/Odoo 18/server/odoo/addons`
   - Confirm your Python path and DB settings are correct.
3. Install from terminal:
   "E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf" -d odoo18 -i student_management --stop-after-init
4. Start server:
   "E:/Odoo 18/python/python.exe" "E:/Odoo 18/server/odoo-bin" -c "E:/Odoo 18/server/odoo.conf"

## Test
- Open http://localhost:8069
- Menu: Student Management → Courses → create a few
- Menu: Student Management → Students → create and enroll using the Courses tab
- Use the buttons on forms to view related records

## Notes from setup
- In Odoo 18 use `<list>` and `view_mode="list,form"`  
- Replace old `attrs` with inline conditions, for example `invisible="enrolled_course_count == 0"`  
- Load order matters in `__manifest__.py`: views first, menus last




