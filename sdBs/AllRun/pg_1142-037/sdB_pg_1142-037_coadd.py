from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[176.238542,-3.948031],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1142-037/sdB_pg_1142-037_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1142-037/sdB_pg_1142-037_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
