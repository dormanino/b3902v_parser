def tojson(self, , output_file_name):
    self.iterable = iterable
    date = datetime.date.today ()
    date_string = date.strftime ('%y%m%d')

    with open (date_string + '_' + 'variant_data_raw', 'w') as f:
        json.dump (iterable, f, indent=4, sort_keys=True, ensure_ascii=False)