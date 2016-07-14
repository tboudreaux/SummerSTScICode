from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[342.256417,1.289789],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_5164/sdB_PB_5164_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_5164/sdB_PB_5164_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
