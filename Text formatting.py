



def time_formatter_short(seconds):
	# Returns columns with values above zero only: (10) Seconds (10:00) Minutes (10:00:00) Hours
	if seconds >= 60:
		minutes = int(seconds / 60)
		if minutes >= 60:
			hours = int(minutes / 60)
			return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02} Hour(s)"
		return f"{minutes:02}:{seconds % 60:02} Minute(s)"
	return f"{seconds:02} Second(s)"


