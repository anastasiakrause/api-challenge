import React, { useEffect, useState } from "react";
import FastAPIClient from "../../client";
import config from "../../config";
import Header from "../../components/Header";
import ReactTable from "../../components/Table";


const client = new FastAPIClient(config);

const Dashboard = () => {
	const [vehicles, setVehicles] = useState([]);

	useEffect(() => {
		fetchVehicleData();
	}, []);

	const fetchVehicleData = () => {
		client.getVehicleData()
			.then((data) => setVehicles(data?.items));
	}

	const columns = React.useMemo(
		() => [
			{
				Header: "Vehicle ID",
				accessor: "vehicle_id" // accessor is the "key" in the data
			},
			{
				Header: "Timestamp",
				accessor: "timestamp"
			},
			{
				Header: "Speed",
				accessor:"speed"
			},
			{
				Header: "Odometer",
				accessor: "odometer"
			},
			{
				Header: "SOC",
				accessor:"soc"
			},
			{
				Header: "Elevation",
				accessor: "elevation"
			},
			{
				Header: "Shift State",
				accessor: "shift_state"
			},
		],
	[]
	);

	// Keep track of data in input fields through state variables and change functions
	const [filterVehicleIDInput, setVehicleIDFilterInput] = React.useState("")
	const [vehicleStartTimestamp, setVehicleStartTimeStamp] = React.useState("")
	const [vehicleEndTimestamp, setVehicleEndTimeStamp] = React.useState("")


    const handleVehicleIDFilterChange = e => {
        const vehicle_id = e.target.value || "";
        setVehicleIDFilterInput(vehicle_id);
    }

	const handleVehicleStartTimestampChange = e => {
        const start_timestamp = e.target.value || "";
        setVehicleStartTimeStamp(start_timestamp);
    }

	const handleVehicleEndTimestampChange = e => {
        const end_timestamp = e.target.value || "";
        setVehicleEndTimeStamp(end_timestamp);
    }

	// Create client request with query parameters when user clicks 'Filter' button
	const queryClient = () =>(
		client.getVehicleDataByID(filterVehicleIDInput, vehicleStartTimestamp, vehicleEndTimestamp).then((data) => setVehicles(data?.items))
	)
	
	return (
		<>
			<section
				className="flex flex-col bg-white text-right"
				style={{ minHeight: "100vh" }}
			>
				<Header />
				<div className="container pt-20 text-left">
					<input
						type="text"
						value={filterVehicleIDInput || ''}
						onChange={handleVehicleIDFilterChange}
						placeholder={"Search Vehicle ID"}
					/>
					<input
						type="text"
						value={vehicleStartTimestamp || ''}
						onChange={handleVehicleStartTimestampChange}
						placeholder={"Start timestamp"}
					/>
					<input
						type="text"
						value={vehicleEndTimestamp || ''}
						onChange={handleVehicleEndTimestampChange}
						placeholder={"End timestamp"}
					/>
					<button onClick={queryClient}> Filter </button>
					<ReactTable data={vehicles} columns={columns}/>
				</div>
			</section>
		</>
	);
};

export default Dashboard;
