from odoo import api, fields, models, _, tools

class SecondModel(models.Model):
    _name = "second.model"
    _description = "Candidate records"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    remote = fields.Boolean(string="Is Remote")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")


class ReportSecondModel(models.AbstractModel):
    _name = 'report.your_module.report_template'
    _description = 'Second Model Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Получите данные для отчета
        docs = self.env['second.model'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'second.model',
            'docs': docs,
        }


class ParticularReport(models.AbstractModel):
    _name = "report.second_module.print_template"
    _description = "Extend of print form"

    @api.model
    def _get_report_values(self, docids, data=None):
        """
        Функция для расширения данных подаваемых на печать в шаблон
        param : docids : list : список id записей модели, к которой прикреплен шаблон для печати
        param : data : {} : дополнительные которые содержат в себе метаинформацию
        return : dict : словарь данными, используемыми в шаблоне
        """
        second_model_recordset = self.env["second.model"].browse(docids)
        ...
        return {
            "doc_ids": docids,
            "docs": second_model_recordset,
            "data": data,
        }