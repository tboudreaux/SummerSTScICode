from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[332.652917,23.684836],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j22106+2341/sdB_galex_j22106+2341_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j22106+2341/sdB_galex_j22106+2341_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
