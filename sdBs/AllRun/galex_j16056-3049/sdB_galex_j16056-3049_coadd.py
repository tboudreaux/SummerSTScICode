from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.400625,-30.820922],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j16056-3049/sdB_galex_j16056-3049_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j16056-3049/sdB_galex_j16056-3049_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
