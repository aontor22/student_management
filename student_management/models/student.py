from odoo import fields, models

class Student(models.Model):
    _name = "student.student"
    _description = "Student Information"

    name = fields.Char(string="Student Name")
    email = fields.Char(string="Email")
    roll_no = fields.Char(string="Roll No")
    department = fields.Char(string="Department")

    course_ids = fields.Many2many(
        comodel_name="student.course",
        relation="student_course_rel",
        column1="student_id",
        column2="course_id",
        string="Enrolled Courses",
    )

    enrolled_course_count = fields.Integer(
        string="Courses",
        compute="_compute_enrolled_course_count",
    )

    def _compute_enrolled_course_count(self):
        for rec in self:
            rec.enrolled_course_count = len(rec.course_ids)

    def action_show_enrolled_courses(self):
        self.ensure_one()
        action = self.env.ref("student_management.action_course").read()[0]
        action["domain"] = [("id", "in", self.course_ids.ids)]
        return action
