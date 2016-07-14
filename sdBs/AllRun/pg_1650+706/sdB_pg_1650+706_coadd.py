from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.580708,70.514475],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1650+706/sdB_pg_1650+706_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1650+706/sdB_pg_1650+706_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
