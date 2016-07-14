from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[197.936917,-8.089719],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1309-078/sdB_pg_1309-078_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1309-078/sdB_pg_1309-078_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()