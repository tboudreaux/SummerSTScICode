from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[268.419042,-50.128278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j175340.57-500741.80/sdB_galex_j175340.57-500741.80_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j175340.57-500741.80/sdB_galex_j175340.57-500741.80_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
