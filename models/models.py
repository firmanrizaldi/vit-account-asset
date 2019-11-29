from odoo import models, fields, api
import time

class vit_accounting_asset(models.Model):
    _name = 'account.asset.asset'
    _inherit = 'account.asset.asset'

    pengadaan = fields.Selection(
    selection=[
        ('PO', 'PO'),
        ('Pembelian Langsung', 'Pembelian Langsung'),
    ],
    string='Metode Pengadaan',
    required="true",
    )
    sertifikat = fields.Selection(
    	selection=[
	    	('SHM', 'SHM'),
	    	('HGB', 'HGB'),
    	],
        string='Jenis Sertifikat',
        required="true",
    )
    processor = fields.Char(
    	string='Processor',
    	size=64,
    	required=False,
    )
    harddisk = fields.Char(
        string='Harddisk',
    )
    memory = fields.Char(
        string='Memory',
    )
    budget = fields.Char(
        string='Budget',
    )
    kd_wilayah = fields.Char(
        string='Kode Wilayah',
    )
    no_polisi = fields.Char(
        string='No. Polisi',
    )
    tgl_pajak = fields.Date(
        string='Tanggal Pajak dan STNK',
        default=lambda self:time.strftime("%Y-%m-%d"),
    )
    tgl_asuransi = fields.Date(
        string='Tanggal Asuransi',
    )
    tanah = fields.Integer(
        string='Luas Tanah',
    )
    bangunan = fields.Integer(
        string='Luas Bangunan',
    )
    no_sertifikat = fields.Char(
        string='Nomor Sertifikat',
    )
    tgl_sertifikat = fields.Date(
        string='Tanggal Sertifikat',
        default=lambda self:time.strftime("%Y-%m-%d"),
    )
    alamat = fields.Text(
        string='Alamat',
    )
    tgl_jp_pajak = fields.Date(
        string='Tanggal Jatuh Tempo Pajak',
        default=lambda self:time.strftime("%Y-%m-%d"),
    )
    tgl_jp_asuransi = fields.Date(
        string='Tanggal Jatuh Tempo Asuransi',
        default=lambda self:time.strftime("%Y-%m-%d"),
    )