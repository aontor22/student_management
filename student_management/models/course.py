from odoo import fields, models

class Course(models.Model):
    _name = "student.course"
    _description = "Course"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    credit = fields.Float()

    student_ids = fields.Many2many(
        comodel_name="student.student",
        relation="student_course_rel",
        column1="course_id",
        column2="student_id",
        string="Enrolled Students",
    )

    enrolled_student_count = fields.Integer(
        string="Students",
        compute="_compute_enrolled_student_count",
    )

    def _compute_enrolled_student_count(self):
        for rec in self:
            rec.enrolled_student_count = len(rec.student_ids)

    def action_show_enrolled_students(self):
        self.ensure_one()
        action = self.env.ref("student_management.action_student").read()[0]
        action["domain"] = [("id", "in", self.student_ids.ids)]
        return action
