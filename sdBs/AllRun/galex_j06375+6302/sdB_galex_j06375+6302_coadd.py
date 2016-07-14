from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[99.387417,63.041306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j06375+6302/sdB_galex_j06375+6302_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j06375+6302/sdB_galex_j06375+6302_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
