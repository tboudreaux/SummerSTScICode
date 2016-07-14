from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.850375,9.797331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1633+099/sdB_pg_1633+099_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1633+099/sdB_pg_1633+099_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
