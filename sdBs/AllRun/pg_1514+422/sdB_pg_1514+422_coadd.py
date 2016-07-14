from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[229.071042,41.984781],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1514+422/sdB_pg_1514+422_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1514+422/sdB_pg_1514+422_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
