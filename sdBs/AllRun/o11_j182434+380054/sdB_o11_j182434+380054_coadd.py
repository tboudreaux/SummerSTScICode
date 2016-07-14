from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[276.141667,38.015],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j182434+380054/sdB_o11_j182434+380054_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j182434+380054/sdB_o11_j182434+380054_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
