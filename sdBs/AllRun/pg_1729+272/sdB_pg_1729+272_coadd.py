from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[262.826292,27.1446],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1729+272/sdB_pg_1729+272_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1729+272/sdB_pg_1729+272_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
