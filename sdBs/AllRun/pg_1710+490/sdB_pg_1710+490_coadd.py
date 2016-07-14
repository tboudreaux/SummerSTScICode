from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[258.078042,48.976639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1710+490/sdB_pg_1710+490_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1710+490/sdB_pg_1710+490_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
