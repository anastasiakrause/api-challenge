import React, { useEffect, useState } from "react";
import FastAPIClient from "../../client";
import config from "../../config";
import Header from "../../components/Header";

import {
	DataGrid,
	GridToolbarContainer,
	GridToolbarExport,
	GridToolbarDensitySelector,
} from '@mui/x-data-grid';

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
		
	function CustomToolbar() {
		return (
		<GridToolbarContainer>
			<GridToolbarExport />
			<GridToolbarDensitySelector />
		</GridToolbarContainer>
		);
	}

	const columns = React.useMemo(
		() => [
			{
				headerName: "ID",
				field: "id"
			},
			{
				headerName: "Vehicle ID",
				field: "vehicle_id" // accessor is the "key" in the data
			},
			{
				headerName: "Timestamp",
				field: "timestamp"
			},
			{
				headerName: "Speed",
				field:"speed"
			},
			{
				headerName: "Odometer",
				field: "odometer"
			},
			{
				headerName: "SOC",
				field:"soc"
			},
			{
				headerName: "Elevation",
				field: "elevation"
			},
			{
				headerName: "Shift State",
				field: "shift_state"
			},
		],
	[]
	);
	
	return (
		<>
			<section
				className="flex flex-col bg-white text-right"
				style={{ minHeight: "100vh" }}
			>
				<Header />
				<div className="container pt-20 text-left">
					<DataGrid
						columns={columns}
						rows={vehicles}
						initialState ={{
							pagination: {
								paginationModel: {pageSize: 10, page: 0}
							}
						}}
						slots={{toolbar: CustomToolbar}}
						autoHeight
					/>
				</div>
			</section>
		</>
	);
};

export default Dashboard;
