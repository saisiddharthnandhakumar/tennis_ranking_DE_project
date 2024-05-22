function transform(line) {
  // Split the input line by commas to extract individual values
  var values = line.split(",");

  // Create an empty JavaScript object to store the values
  var obj = new Object();

  // Assign values to the object properties based on their position in the input string
  obj.player_name = values[0];
  obj.rank = parseInt(values[1], 10); // Convert to integer using parseInt()
  obj.country = values[2];
  obj.points = parseInt(values[3], 10); // Convert to integer using parseInt()

  // Convert the JavaScript object to a JSON string
  var jsonString = JSON.stringify(obj);

  // Return the JSON string
  return jsonString;
}
