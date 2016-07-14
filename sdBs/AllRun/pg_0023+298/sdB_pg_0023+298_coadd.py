from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[6.473792,30.086989],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0023+298/sdB_pg_0023+298_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0023+298/sdB_pg_0023+298_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
