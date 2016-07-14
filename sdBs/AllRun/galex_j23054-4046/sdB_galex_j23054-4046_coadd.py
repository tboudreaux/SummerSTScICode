from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[346.356125,-40.776181],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j23054-4046/sdB_galex_j23054-4046_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j23054-4046/sdB_galex_j23054-4046_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
