from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.309667,69.493514],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1633+696/sdB_pg_1633+696_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1633+696/sdB_pg_1633+696_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
