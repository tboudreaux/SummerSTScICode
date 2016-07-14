from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.195875,35.345383],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1646+354/sdB_pg_1646+354_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1646+354/sdB_pg_1646+354_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
