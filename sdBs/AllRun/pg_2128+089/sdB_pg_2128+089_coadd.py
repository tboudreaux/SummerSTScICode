from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[322.771667,9.131708],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2128+089/sdB_pg_2128+089_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2128+089/sdB_pg_2128+089_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
