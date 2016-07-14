from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[312.47525,-69.608808],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j20499-6936/sdB_galex_j20499-6936_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j20499-6936/sdB_galex_j20499-6936_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
