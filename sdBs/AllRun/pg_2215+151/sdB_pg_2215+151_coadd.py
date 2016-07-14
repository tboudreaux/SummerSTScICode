from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[334.450792,15.349053],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2215+151/sdB_pg_2215+151_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2215+151/sdB_pg_2215+151_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
