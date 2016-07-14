from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[294.418292,-43.065706],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J19376-4303/sdB_GALEX_J19376-4303_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J19376-4303/sdB_GALEX_J19376-4303_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
