def CheckAvailability(currCheckinDate,currCheckoutDate):
	if currCheckoutDate:
		querry=select RoomNo from visitors where (CheckindDate is not null and CheckoutDate is not null and ((currCheckinDate<CheckinDate and currCheckoutDate<= CheckinDate) or (currCheckinDate > CheckoutDate) or (currCheckoutDate<=CheckinDate))) or (CheckinDate is null and CheckoutDate is null);
		pass
	else:
		querry=slect RoomNo from visitors where (currCheckinDate<CheckinDate) or ((CheckinDate is not null and CheckoutDate is not null) and currCheckinDate>CheckoutDate) or (((CheckinDate is not null and CheckoutDate is not null) and currCheckinDate<CheckinDate)); 
	pass

def DeskBooking($_POST):
	BookRoom= $_POST.split(",")
	for i in BookRoom:
		RoomBooking(BookRoom[i])
		pass
	pass

def RoomBooking():
	querry=Insert into visitors values("a", "Name", "Gender", "PhoneNo", "Visitorsid", "CheckinDate", "CheckoutDate", "RoomNo" )
	pass

