from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.120083,14.847067],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1602+149/sdB_pg_1602+149_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1602+149/sdB_pg_1602+149_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()